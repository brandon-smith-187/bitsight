from enum import Enum

from bitsight.api_io.request_handler import RequestHandler


class BitSight:
    def __init__(self):
        self._handler = RequestHandler()
        self._BASE_URL = 'https://api.bitsighttech.com/'

    def get(self, endpoint, **kwargs):
        """
        method for wrapping get requests and handling certain status codes
        :param endpoint: the url for the endpoint
        :return: response object
        """
        return self._handler.get(request_url=f"{self._BASE_URL}{endpoint}", **kwargs)

    def post(self, endpoint, json, **kwargs):
        """
        method for handling a post request
        :param json: the payload to post
        :param endpoint: the url for the endpoint
        :return: response object
        """
        return self._handler.post(request_url=f"{self._BASE_URL}{endpoint}", json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        """
        method for handling delete requests
        :param endpoint: the url to process for the DELETE request
        :return: response object with status code, text, etc.
        """
        return self._handler.delete(request_url=f"{self._BASE_URL}{endpoint}", **kwargs)


class Endpoints:
    class V1(Enum):
        overview = ''
        enable_vendor_access = 'access-requests/'
        companies = 'companies/'
        company_relationships = 'company-relationships/'
        company_requests = 'company-requests/'
        customers = 'customers/'
        defaults = 'defaults/'
        exposed_credentials = 'exposed-credentials/'
        wfh = 'findings/wfh/'
        folders = 'folders/'
        industries = 'industries/'
        news = 'news/'
        peer_analytics = 'peer-analytics/'
        portfolio = 'portfolio/'
        fast_ratings = 'fast-ratings/'
        reports = 'reports/'
        subscriptions = 'subscriptions/'
        territories = 'territories/'
        tiers = 'tiers/'

        def __init__(self, path):
            self.path = path

        def __str__(self):
            return f"{self.__class__.__name__.lower()}/{self.path}"

    class V2(Enum):
        overview = ''
        alerts = 'alerts/'
        company_requests = 'company-requests/'
        portfolio = 'portfolio/'
        users = 'users/'

        def __init__(self, path):
            self.path = path

        def __str__(self):
            return f"{self.__class__.__name__.lower()}/{self.path}"
