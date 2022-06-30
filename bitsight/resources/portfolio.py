from bitsight.api_io.request_handler import RequestHandler, pagination


class Portfolio:
    PORTFOLIO_ENDPOINT = "https://api.bitsighttech.com/v2/portfolio"

    def __init__(self):
        self.handler = RequestHandler()

    @pagination
    # @threaded_pagination
    def get_portfolio(self, folder=None, params=None, request_url=None, cookies=None):
        """
        Get all companies in your portfolio
        :param folder: guid for the folder containing the companies
        :param params: filters for the request
        :param request_url: the url for the request
        :param cookies: cookies for the request
        :return: json representation of all companies
        """
        if request_url is None:
            request_url = self.PORTFOLIO_ENDPOINT
        if folder is not None:
            parameters = {'folder': folder}
        else:
            parameters = {}
        if params is not None:
            parameters.update(params)
        return self.handler.get(request_url=request_url, params=parameters, cookies=cookies)
