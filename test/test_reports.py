from unittest import TestCase

from bitsight.resources.reports import Reports


class TestReports(TestCase):
    reports = Reports()

    def test_post_request_company_report(self):
        reports_folder = '/Users/brandonsmith/Documents/bitsight/test/test-files/'
        name = 'ABB'
        raised_exception = False
        try:
            report = self.reports.post_request_company_report(guid='46c3f7e8-999d-426d-9953-5ae9a91a0f97')
            with open(reports_folder + name + ".pdf", 'wb') as pdf_file:
                pdf_file.write(report.content)
        except:
            raised_exception = True
        self.assertFalse(raised_exception)
