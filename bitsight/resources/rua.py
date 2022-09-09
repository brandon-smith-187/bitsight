from bitsight.resources.bitsight import BitSight, Endpoints


class RapidUnderwriting(BitSight):
    v1_endpoint = f"{Endpoints.V1.fast_ratings}"

    def __init__(self):
        super().__init__()

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
            "industry": f"{industry}",
        }

        return self.post(endpoint=self.v1_endpoint, json=payload, **kwargs).json()

    def get_rua_quota(self, **kwargs):
        """
        Get remaining rua licenses
        :return: json representation of remaining rua licenses
        """
        return self.get(endpoint=self.v1_endpoint + "quota", **kwargs)
