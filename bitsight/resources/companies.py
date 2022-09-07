from bitsight.api_io.request_handler import RequestHandler


class Companies:
    V1_ENDPOINT = "https://api.bitsighttech.com/v1/companies/"

    def __init__(self):
        super().__init__()
        self.handler = RequestHandler()

    # @pagination
    def get_findings(self, guid, params=None, **kwargs):
        """
        Get all findings for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of all applicable findings
        """
        request_url = self.V1_ENDPOINT + guid + "/findings"

        return self.handler.get(request_url=request_url, params=params, **kwargs)

    def get_company_details(self, guid, params=None, **kwargs):
        """
        Get ratings and risk vectors for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of the details for the company
        """
        return self.handler.get(request_url=self.V1_ENDPOINT + guid, params=params, **kwargs)

    def get_company_search(self, domain, params=None, **kwargs):
        """
        Search for a company based on a provided domain
        :param domain: the domain to search based on
        :param params: filters for the request
        :return: json representation of all search results
        """
        request_url = self.V1_ENDPOINT + "/search"

        if params is None:
            params = {'domain': domain}
        else:
            params.update({'domain': domain})

        return self.handler.get(request_url=request_url, params=params, **kwargs)
