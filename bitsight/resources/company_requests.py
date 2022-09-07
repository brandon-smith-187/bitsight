from bitsight.api_io.request_handler import RequestHandler


class CompanyRequests:
    V2_ENDPOINT = "https://api.bitsighttech.com/v2/company-requests/"

    def __init__(self):
        super().__init__()
        self.handler = RequestHandler()

    def get_request_status(self, guid, params=None, **kwargs):
        """
        Get the status of a request
        :param guid: the guid for the request
        :param params: filters for the request
        :return: json representation of request details
        """

        return self.handler.get(request_url=self.V2_ENDPOINT + guid, params=params, **kwargs)

    def get_all_company_requests(self, params=None, **kwargs):
        """
        Get details on all company requests
        :param params: filters for the request
        :return: json representation of details on all company requests
        """

        return self.handler.get(request_url=self.V2_ENDPOINT, params=params, **kwargs)

    def post_request_company(self, domain, subscription_type=None, **kwargs):
        """
        Request to subscribe to a company in BitSight
        :param subscription_type: the license type to use to subscribe
        :param domain: the domain for the company you are requesting
        :return: json confirmation
        """
        if subscription_type is not None:
            payload = {"domain": domain, "subscription_type": subscription_type}
        else:
            payload = {"domain": domain}

        return self.handler.post(self.V2_ENDPOINT, json=payload, **kwargs).json()
