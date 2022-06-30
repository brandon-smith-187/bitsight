def get_portfolio(self, folder=None):
    """
    Get all companies in your portfolio
    :param folder: guid for the folder containing the companies
    :return: json representation of all companies
    """
    request_url = self.PORTFOLIO_ENDPOINT
    headers = {"Accept": "application/json"}
    if folder is not None:
        parameters = {'folder': folder}
    else:
        parameters = {}
    response = self._get_request_handler(
        request_url, parameters, headers=headers
    ).json()
    companies = response[RESULTS]
    while response[LINKS][NEXT]:
        response = self._get_request_handler(
            response[LINKS][NEXT], headers=headers
        ).json()
        companies.extend(response[RESULTS])
    return companies
