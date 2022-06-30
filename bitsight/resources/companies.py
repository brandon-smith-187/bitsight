from bitsight.api_io.request_handler import RequestHandler, pagination


class Companies:
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
