from bitsight.api_io.request_handler import RequestHandler


class Reports:
    V1_ENDPOINT = 'https://api.bitsighttech.com/v1/reports/'

    def __init__(self):
        super().__init__()
        self.handler = RequestHandler()

    def post_download_company_report(self, guid, file_path='company_report.pdf', **kwargs):
        """
        Request to download a company report from BitSight
        :param file_path: path for saving the file
        :param guid: the guid for the company you are requesting
        """
        json = {"params": {"company": guid}}
        headers = {"Accept": "application/pdf"}

        pdf_reponse = self.handler.post(self.V1_ENDPOINT, json=json, headers=headers, **kwargs)

        with open(file_path, 'wb') as pdf_file:
            pdf_file.write(pdf_reponse.content)
        return pdf_reponse.status_code < 400
