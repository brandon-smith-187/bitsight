from bitsight.resources.bitsight import BitSight, Endpoints, QueryParams, LicenseType


class CompanyRequests(BitSight):
    v2_endpoint = f"{Endpoints.V2.company_requests}"

    def __init__(self, api_key: str | None = None):
        super().__init__(api_key)

    def get_request_status(self, guid: str, params: QueryParams = None, **kwargs):
        """
        Get the status of a request
        :param guid: the guid for the request
        :param params: filters for the request
        :return: json representation of request details
        """

        return self.get(endpoint=self.v2_endpoint + guid, params=params, **kwargs)

    def get_all_company_requests(self, params: QueryParams = None, **kwargs):
        """
        Get details on all company requests
        :param params: filters for the request
        :return: json representation of details on all company requests
        """

        return self.get(endpoint=self.v2_endpoint, params=params, **kwargs)

    def post_request_company(
        self, domain: str, subscription_type: str | LicenseType | None = None, **kwargs
    ):
        """
        Request to subscribe to a company in BitSight
        :param subscription_type: the license type to use to subscribe when the company is available
        :param domain: the domain for the company you are requesting
        :return: json confirmation
        """
        if subscription_type is not None:
            payload = {"domain": domain, "subscription_type": f"{subscription_type}"}
        else:
            payload = {"domain": domain}

        return self.post(endpoint=self.v2_endpoint, json=payload, **kwargs).json()
