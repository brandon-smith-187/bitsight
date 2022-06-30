from bitsight.api_io.request_handler import RequestHandler


class Reports:
    REPORTS_ENDPOINT = 'https://api.bitsighttech.com/v1/reports/'

    def __init__(self):
        self.handler = RequestHandler()

    def post_request_company_report(self, guid):
        """
        Request to download a company report from BitSight
        :param guid: the guid for the company you are requesting
        :return: response object with report data in content that can be saved as a pdf
        """
        json = {"params": {"company": guid}}
        headers = {"Accept": "application/pdf"}

        return self.handler.post(self.REPORTS_ENDPOINT, json=json, headers=headers)
