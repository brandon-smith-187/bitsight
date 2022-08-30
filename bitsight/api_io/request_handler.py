import datetime
import os
import threading
import time
from enum import Enum
from functools import wraps

import requests


class Status(Enum):
    okay = (200, "Everything worked as expected")
    success = (201, "The request was successfully submitted")
    no_authentication = (401, "No valid API token was provided")
    unauthorized = (403, "You do not have permission to access this resource")
    not_found = (404, "The specified resource does not exist")
    rate_limited = (429, "Rate Limit Reached")
    server_error = (500, "Something went wrong on the BitSight end")
    time_out = (524, "The connection to the web server was successful, but the connection timed out")

    def __init__(self, code, description):
        self.code = code
        self.description = description


"""Use threading for pagination"""
THREADED_PAGINATION = True

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
    If THREADED_PAGINATION is true, then the pagination is processed by concurrent
    threds, otherwise it is processed in serial
    :param func: the function to process for paginated output
    :return: total result of all calls as a json
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    @wraps(func)
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        response_json = first.json()
        results = response_json[RESULTS]
        count = response_json['count']
        total_req_number = int(count / 100)
        if count % 100 != 0:
            total_req_number += 1

        if THREADED_PAGINATION:
            params = kwargs.get('params', {})
            param_list = [{'limit': 100, 'offset': str(n * 100)} for n in range(1, total_req_number)]
            threads = []
            max_threads = 3
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                for param in param_list:
                    param.update(params)
                    kwargs['params'] = param
                    kwargs['cookies'] = first.cookies
                    threads.append(executor.submit(func, *args, **kwargs))

                for task in as_completed(threads):
                    results.extend(task.result().json()[RESULTS])
        else:
            links = first.json().get(LINKS)

            while links.get(NEXT):
                kwargs['cookies'] = first.cookies
                kwargs['request_url'] = links.get(NEXT)
                response = func(*args, **kwargs)
                links = response.json().get(LINKS)
                results.extend(response.json()[RESULTS])

        return results

    return wrapper


class RequestHandler:
    """
    Class for handling calls to the BitSight API
    Uses the singleton design pattern to prevent duplicate instances and to keep the backoff factor
    consistent
    """
    factor = 0.0
    GROWTH_FACTOR = 0.3
    base_wait_time = ONE_MINUTE
    HEADERS = {"Accept": "application/json"}
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
        self.api_key = os.environ.get(BST_API_KEY)
        if self.api_key is None or self.api_key == EMPTY_STRING:
            self.api_key = input("Please enter your BitSight API Kry: ")
        self.today = datetime.date.today()

    def get(self, request_url, params=None, headers=None, cookies=None):
        """
        Private helper method for wrapping get requests and handling certain status codes
        :param request_url: the url for the endpoint
        :param params: parameters for the request (optional)
        :param headers: headers for the request (optional)
        :param cookies: cookies for the request (optional)
        :return: response object
        """
        if headers is None:
            headers = self.HEADERS
        try:
            response = requests.get(
                request_url,
                auth=(self.api_key, EMPTY_STRING),
                params=params,
                headers=headers,
                cookies=cookies
            )

            while response.status_code == Status.rate_limited.code:
                retry_after = float(response.headers[RETRY_AFTER])
                self.back_off(retry_after=retry_after, status_code=response.status_code)
                response = requests.get(
                    request_url,
                    auth=(self.api_key, EMPTY_STRING),
                    params=params,
                    headers=headers,
                )

            while response.status_code >= Status.server_error.code:
                self.back_off(status_code=response.status_code)
                response = requests.get(
                    request_url,
                    auth=(self.api_key, EMPTY_STRING),
                    params=params,
                    headers=headers,
                )

            if response.status_code == Status.unauthorized.code:
                # added due to odd issue where a 403 was returned and the text content was a html page
                # suspected to be cloudflare DDoS protection
                print(response.request.url)
                print(response.request.headers)
                print(response.text)
                # retry once after a period of time
                self.back_off(status_code=response.status_code)
                response = requests.get(
                    request_url,
                    auth=(self.api_key, EMPTY_STRING),
                    params=params,
                    headers=headers
                )
                # if response after waiting a minute, raise an exception
                if response.status_code == Status.unauthorized.code:
                    raise requests.exceptions.ConnectionError("Random 403 error, output incomplete")

            self.factor = 0.0
            return response
        except requests.exceptions.HTTPError as http_error:
            print(http_error)
        except requests.exceptions.ConnectionError as connection_error:
            print(connection_error)
        except requests.exceptions.Timeout as timeout_error:
            print(timeout_error)
        except requests.exceptions.RequestException as request_error:
            print(request_error)

    def post(self, request_url, params=None, json=None, headers=None):
        """
        Private method for handling a post request and any needed retries
        :param request_url: the url for the endpoint
        :param params: parameters for the request (optional)
        :param json: the json to POST
        :param headers: headers for the request (optional)
        :return: response object
        """
        if headers is None:
            headers = self.HEADERS
        response = requests.post(request_url, auth=(self.api_key, EMPTY_STRING), params=params, json=json,
                                 headers=headers)
        while response.status_code == Status.rate_limited.code:
            retry_after = float(response.headers[RETRY_AFTER])
            self.back_off(retry_after=retry_after, status_code=response.status_code)
            response = requests.post(request_url, auth=(self.api_key, EMPTY_STRING), params=params, json=json,
                                     headers=headers)

        while response.status_code >= Status.server_error.code:
            self.back_off(status_code=response.status_code)
            response = requests.post(request_url, auth=(self.api_key, EMPTY_STRING), params=params, json=json,
                                     headers=headers)

        self.factor = 0.0
        return response

    def delete(self, request_url, headers=None):
        """
        Handles delete requests and handles rate limiting
        :param request_url: the url to process for the DELETE request
        :param headers: the headers for the request
        :return: response object with status code, text, etc.
        """
        if headers is None:
            headers = self.HEADERS
        response = requests.delete(request_url, auth=(self.api_key, EMPTY_STRING), headers=headers)
        while response.status_code == Status.rate_limited.code:
            retry_after = float(response.headers[RETRY_AFTER])
            self.back_off(retry_after=retry_after, status_code=response.status_code)
            response = requests.delete(request_url, auth=(self.api_key, EMPTY_STRING), headers=headers)

        while response.status_code >= Status.server_error.code:
            self.back_off(status_code=response.status_code)
            response = requests.delete(request_url, auth=(self.api_key, EMPTY_STRING), headers=headers)

        self.factor = 0.0
        return response

    def back_off(self, retry_after=None, status_code=None):
        """
        Method for handling a retry as well as raising the backoff factor
        :param retry_after: the period of time specified to retry after (passed from api response)
        :param status_code: the status code of the response (passed from the api response)
        """
        print(f'Response Code: {status_code}')
        if retry_after is not None:
            self.base_wait_time = retry_after
            wait_time = retry_after * (1.0 + self.factor)
        else:
            wait_time = self.base_wait_time * (1.0 + self.factor)
        print(f'Error or Rate Limiting: Retrying in {wait_time} seconds')
        self.factor += self.GROWTH_FACTOR
        time.sleep(wait_time)
