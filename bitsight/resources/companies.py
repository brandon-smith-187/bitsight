from bitsight.resources.bitsight import BitSight, Endpoints


class Companies(BitSight):
    v1_endpoint = f"{Endpoints.V1.companies}"

    def __init__(self):
        super().__init__()

    def get_findings(self, guid, params=None, **kwargs):
        """
        Get all findings for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of all applicable findings
        """
        endpoint = self.v1_endpoint + guid + "/findings"

        return self.get(endpoint=endpoint, params=params, **kwargs)

    def get_company_details(self, guid, params=None, **kwargs):
        """
        Get ratings and risk vectors for a company
        :param guid: the BitSight guid for the company
        :param params: filters for the request
        :return: json representation of the details for the company
        """
        return self.get(endpoint=self.v1_endpoint + guid, params=params, **kwargs)

    def get_company_search(self, domain, params=None, **kwargs):
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
