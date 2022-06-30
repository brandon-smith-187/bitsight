from bitsight.api_io.request_handler import RequestHandler


class Reports:
    REPORTS_ENDPOINT = 'https://api.bitsighttech.com/v1/reports/'

    def __init__(self):
        self.handler = RequestHandler()

    def post_request_report(self, guid):
        """
        Request to download a company report from BitSight
        :param guid: the guid for the company you are requesting
        :return: response object with report data in content
        """
        json = {"params": {"company": guid}}

        return self.handler.post(self.REPORTS_ENDPOINT, json=json)
