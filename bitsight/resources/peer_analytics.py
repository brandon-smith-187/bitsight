from bitsight.api_io.request_handler import RequestHandler, pagination


class PeerAnalytics:
    COMPANIES_ENDPOINT = "https://api.bitsighttech.com/v1/companies/"

    def __init__(self):
        self.handler = RequestHandler()

    @pagination
    def get_findings(self, guid=None, params=None, request_url=None, cookies=None):
        """
        Get all findings for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :param request_url: the url for the request
        :param cookies: cookies for the request
        :return: json representation of all applicable findings
        """
        if request_url is None:
            request_url = self.COMPANIES_ENDPOINT + guid + "/findings"

        return self.handler.get(request_url=request_url, params=params, cookies=cookies)

    def get_company_details(self, guid=None, params=None, cookies=None):
        """
        Get ratings and risk vectors for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :param cookies: cookies for the request
        :return: json representation of the details for the company
        """
        return self.handler.get(request_url=self.COMPANIES_ENDPOINT + guid, params=params, cookies=cookies).json()

    @pagination
    def get_company_search(self, domain=None, params=None, request_url=None, cookies=None):
        """
        Search for a company based on a provided domain
        :param domain: the domain to search based on
        :param params: filters for the request
        :param request_url: the url for the request
        :param cookies: cookies for the request
        :return: json representation of all search results
        """
        if request_url is None:
            request_url = self.COMPANIES_ENDPOINT + "/search"

        if params is None:
            params = {'domain': domain}
        else:
            params.update({'domain': domain})

        return self.handler.get(request_url=request_url, params=params, cookies=cookies)
