from bitsight.api_io.request_handler import RequestHandler, pagination


class Portfolio:
    V2_PORTFOLIO_ENDPOINT = "https://api.bitsighttech.com/v2/portfolio/"
    V1_PORTFOLIO_ENDPOINT = "https://api.bitsighttech.com/v1/portfolio/"

    def __init__(self):
        self.handler = RequestHandler()

    @pagination
    def get_portfolio(self, folder=None, params=None, request_url=None, cookies=None, headers=None):
        """
        Get all companies in your portfolio
        :param folder: guid for the folder containing the companies
        :param params: filters for the request
        :param request_url: the url for the request
        :param cookies: cookies for the request
        :param headers: the headers to include with the request
        :return: json representation of all companies
        """
        if request_url is None:
            request_url = self.V2_PORTFOLIO_ENDPOINT
        if folder is not None:
            parameters = {'folder': folder}
        else:
            parameters = {}
        if params is not None:
            parameters.update(params)
        return self.handler.get(request_url=request_url, params=parameters, cookies=cookies, headers=headers)

    def get_infected_companies(self, infections=None, params=None, headers=None):
        """
        Get all companies in your portfolio impacted by the specified infection
        :param infections: the infection(s) to search for
        :param params: filters for the request
        :param headers: the headers to include with the request
        :return: json representation of all companies that are impacted
        """
        parameters = {'infections': infections}
        if params is not None:
            parameters.update(params)

        return self.get_portfolio(params=parameters, headers=headers)

    def get_vulnerable_companies(self, vulnerabilities=None, params=None, headers=None):
        """
        Get all companies in your portfolio impacted by the specified infection
        :param vulnerabilities: the vulnerability(or vulnerabilities) to search for
        :param params: filters for the request
        :param headers: the headers to include with the request
        :return: json representation of all companies that are impacted
        """
        parameters = {'vulnerabilities': vulnerabilities}
        if params is not None:
            parameters.update(params)

        return self.get_portfolio(params=parameters, headers=headers)

    def get_portfolio_statics(self, params=None, cookies=None, headers=None):
        """
        Get statistics for your entire portfolio
        :param params: filters for the request
        :param cookies: cookies for the request
        :param headers: the headers to include with the request
        :return: json representation of statistics for your portfolio
        """
        return self.handler.get(request_url=self.V1_PORTFOLIO_ENDPOINT + 'statistics', params=params, cookies=cookies,
                                headers=headers)
