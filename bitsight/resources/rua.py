from bitsight.api_io.request_handler import RequestHandler


class RapidUnderwriting:
    V1_ENDPOINT = 'https://api.bitsighttech.com/ratings/v1/fast-ratings/'

    def __init__(self):
        super().__init__()
        self.handler = RequestHandler()

    def post_request_rua(self, domain, company_name, industry, **kwargs):
        """
        Request to subscribe to a company in BitSight
        :param industry: industry for the company
        :param domain: the domain to request the RUA for
        :param company_name: the name of the company
        :return: json representation of the rua report
        """
        payload = {
            "company": company_name,
            "url": domain,
            "generate_report": "true",
            "industry": industry
        }

        return self.handler.post(self.V1_ENDPOINT, json=payload, **kwargs)

    def get_rua_quota(self, **kwargs):
        """
        Get ratings and risk vectors for a company
        :return: json representation of the details for the company
        """
        return self.handler.get(request_url=self.V1_ENDPOINT + 'quota', **kwargs)
