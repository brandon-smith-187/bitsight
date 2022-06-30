def post_request_report(self, guid):
    """
    Request to download a company report from BitSight
    :param guid: the guid for the company you are requesting
    :return: response object with report data in content
    """
    json = {"params": {"company": guid}}

    reports_request = self._post_request_handler(self.REPORTS_ENDPOINT, json=json)
    return reports_request
