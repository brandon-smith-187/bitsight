from bitsight.resources.bitsight import BitSight, Endpoints


class Portfolio(BitSight):
    v2_endpoint = f"{Endpoints.V2.portfolio}"
    v1_endpoint = f"{Endpoints.V1.portfolio}"

    def __init__(self):
        super().__init__()

    def get_portfolio(self, folder=None, params=None, **kwargs):
        """
        Get all companies in your portfolio
        :param folder: guid for the folder containing the companies
        :param params: filters for the request
        :return: json representation of all companies
        """
        request_url = self.v2_endpoint
        if folder is not None:
            parameters = {"folder": folder}
        else:
            parameters = {}
        if params is not None:
            parameters.update(params)
        return self.get(endpoint=request_url, params=parameters, **kwargs)

    def get_infected_companies(self, infections, params=None, **kwargs):
        """
        Get all companies in your portfolio impacted by the specified infection
        :param infections: the infection(s) to search for
        :param params: filters for the request
        :return: json representation of all companies that are impacted
        """
        parameters = {"infections": infections}
        if params is not None:
            parameters.update(params)

        return self.get_portfolio(params=parameters, **kwargs)

    def get_vulnerable_companies(self, vulnerabilities, params=None, **kwargs):
        """
        Get all companies in your portfolio impacted by the specified infection
        :param vulnerabilities: the vulnerability(or vulnerabilities) to search for
        :param params: filters for the request
        :return: json representation of all companies that are impacted
        """
        parameters = {"vulnerabilities": vulnerabilities}
        if params is not None:
            parameters.update(params)

        return self.get_portfolio(params=parameters, **kwargs)

    def get_portfolio_statistics(self, params=None, **kwargs):
        """
        Get statistics for your entire portfolio
        :param params: filters for the request
        :return: json representation of statistics for your portfolio
        """
        return self.get(
            endpoint=self.v1_endpoint + "statistics", params=params, **kwargs
        )
