from bitsight.resources.bitsight import BitSight, Endpoints, QueryParams


class Companies(BitSight):
    v1_endpoint = f"{Endpoints.V1.companies}"

    def __init__(self, api_key: str | None = None):
        super().__init__(api_key)

    def get_findings(self, guid: str, params: QueryParams = None, **kwargs):
        """
        Get all findings for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of all applicable findings
        """
        endpoint = self.v1_endpoint + guid + "/findings"

        return self.get(endpoint=endpoint, params=params, **kwargs)

    def get_company_details(self, guid: str, params: QueryParams = None, **kwargs):
        """
        Get ratings and risk vectors for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of the details for the company
        """
        return self.get(endpoint=self.v1_endpoint + guid, params=params, **kwargs)

    def get_company_search(self, domain: str, params: QueryParams = None, **kwargs):
        """
        Search for a company based on a provided domain
        :param domain: the domain to search based on
        :param params: filters for the request
        :return: json representation of all search results
        """
        endpoint = self.v1_endpoint + "/search"

        if params is None:
            params = {"domain": domain}
        else:
            params.update({"domain": domain})

        return self.get(endpoint=endpoint, params=params, **kwargs)

    def get_assets(self, guid: str, params: QueryParams = None, **kwargs):
        """
        Get a company's asset information (domains and IP addresses)
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of the search results
        """
        endpoint = self.v1_endpoint + guid + "/assets"

        return self.get(endpoint=endpoint, params=params, **kwargs)
