import os
import threading
import time
from enum import Enum
from functools import wraps
import logging

import requests


class Status(Enum):
    okay = (200, "Everything worked as expected")
    success = (201, "The request was successfully submitted")
    entity_queued = (202, "Entity queued")
    no_authentication = (401, "No valid API token was provided")
    unauthorized = (403, "You do not have permission to access this resource")
    not_found = (404, "The specified resource does not exist")
    rate_limited = (429, "Rate Limit Reached")
    server_error = (500, "Something went wrong on the BitSight end")
    time_out = (
        524,
        "The connection to the web server was successful, but the connection timed out",
    )

    def __init__(self, code, description):
        self.code = code
        self.description = description


"""Number of seconds in a minute"""
ONE_MINUTE = 60.0

"""Empty string, used for auth password"""
EMPTY_STRING = ""

"""next key in api response when there is pagination"""
NEXT = "next"

"""links key in api response when there is pagination"""
LINKS = "links"

"""results key in api response, which contains results"""
RESULTS = "results"

"""Retry-After header returned with a 429 status codes.
Specifies the number of seconds to wait before retrying the request"""
RETRY_AFTER = "Retry-After"

"""Environment variable to set containing your BitSight API key"""
BST_API_KEY = "BST_API_KEY"


def pagination(func):
    """
    Decorator to add to a function to process an endpoint with a paginated return
    :param func: the function to process for paginated output
    :return: total result of all calls as a json
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        response_json = first.json()
        results = response_json.get(RESULTS)
        if results:
            try:
                links = first.json().get(LINKS)

                while links.get(NEXT):
                    kwargs["request_url"] = links.get(NEXT)
                    response = func(*args, **kwargs)
                    links = response.json().get(LINKS)
                    results.extend(response.json()[RESULTS])

                return results
            except AttributeError:
                return response_json
        else:
            return response_json

    return wrapper


class RequestHandler(requests.Session):
    """
    Class for handling calls to the BitSight API
    Uses the singleton design pattern to prevent duplicate instances and to keep the backoff factor
    consistent
    """

    factor = 0.0
    GROWTH_FACTOR = 0.3
    base_wait_time = ONE_MINUTE
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(RequestHandler, cls).__new__(cls)
                    cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        super().__init__()
        self.api_key = os.environ.get(BST_API_KEY)

        if self.api_key is None or self.api_key == EMPTY_STRING:
            self.api_key = input("Please enter your BitSight API Key: ")

        self.auth = (self.api_key, EMPTY_STRING)
        self.headers.update({"Accept": "application/json"})
        logging.basicConfig(level=logging.INFO)

    def _bitsight_request(self, method, request_url, **kwargs):
        try:
            response = self.request(method, request_url, **kwargs)

            while response.status_code == Status.rate_limited.code:
                retry_after = float(response.headers[RETRY_AFTER])
                self.back_off(retry_after=retry_after, status_code=response.status_code)
                response = self.request(method, request_url, **kwargs)

            while response.status_code == Status.entity_queued.code:
                self.back_off(status_code=response.status_code)
                response = self.request(method, request_url, **kwargs)

            while response.status_code >= Status.server_error.code:
                self.back_off(status_code=response.status_code)
                response = self.request(method, request_url, **kwargs)

            if response.status_code == Status.unauthorized.code:
                # added due to odd issue where a 403 was returned and the text content was a html page
                # suspected to be cloudflare DDoS protection
                response_json = response.json()
                if (
                        response_json.get("detail") is None
                        or response_json.get("detail")
                        != "You do not have permission to perform this action."
                ):
                    logging.info(f"Request URL: {response.request.url}")
                    logging.info(f"Request Headers: {response.request.headers}")
                    logging.info(f"Response Text: {response.text}")
                    # retry once after a period of time
                    self.back_off(status_code=response.status_code)
                    response = self.request(method, request_url, **kwargs)
                    # if response after waiting a minute, raise an exception
                    if response.status_code == Status.unauthorized.code:
                        raise requests.exceptions.ConnectionError(
                            "Random 403 error, output incomplete"
                        )

            self.factor = 0.0
            return response
        except requests.exceptions.HTTPError as http_error:
            logging.error(str(http_error))
        except requests.exceptions.ConnectionError as connection_error:
            logging.error(str(connection_error))
        except requests.exceptions.Timeout as timeout_error:
            logging.error(str(timeout_error))
        except requests.exceptions.RequestException as request_error:
            logging.error(str(request_error))

    @pagination
    def get(self, request_url, **kwargs):
        """
        method for wrapping get requests and handling certain status codes
        :param request_url: the url for the endpoint
        :return: response object
        """
        return self._bitsight_request("GET", request_url, **kwargs)

    def post(self, request_url, **kwargs):
        """
        method for handling a post request
        :param request_url: the url for the endpoint
        :return: response object
        """
        return self._bitsight_request("POST", request_url, **kwargs)

    def delete(self, request_url, **kwargs):
        """
        method for handling delete requests
        :param request_url: the url to process for the DELETE request
        :return: response object with status code, text, etc.
        """
        return self._bitsight_request("DELETE", request_url, **kwargs)

    def patch(self, request_url, **kwargs):
        """
        method for handling a patch request
        :param request_url: the url for the endpoint
        :return: response object
        """
        return self._bitsight_request("PATCH", request_url, **kwargs)

    def back_off(self, retry_after=None, status_code=None):
        """
        Method for handling a retry as well as raising the backoff factor
        :param retry_after: the period of time specified to retry after (passed from api response)
        :param status_code: the status code of the response (passed from the api response)
        """
        logging.info(f"Response Code: {status_code}")
        if retry_after is not None:
            self.base_wait_time = retry_after
            wait_time = retry_after * (1.0 + self.factor)
        else:
            wait_time = self.base_wait_time * (1.0 + self.factor)
        logging.info(f"Error or Rate Limiting: Retrying in {wait_time} seconds")
        self.factor += self.GROWTH_FACTOR
        time.sleep(wait_time)
