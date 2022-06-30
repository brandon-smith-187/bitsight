from unittest import TestCase

from bitsight.resources.companies import Companies


class TestCompanies(TestCase):
    companies = Companies()

    def test_get_findings(self):
        params = {'affects_rating': 'true'}
        findings = self.companies.get_findings(guid='97a6a734-b16f-47c2-a3c1-4f08358821a3', params=params)
        # print(findings)
        self.assertEqual(326, len(findings))

    def test_get_company_search(self):
        companies = self.companies.get_company_search(domain='a360inc.com')
        self.assertEqual(1000, len(companies))

    def test_get_company_details(self):
        company = self.companies.get_company_details(guid='7983f37b-31fc-4948-8fcd-994f48fe0da4')
        self.assertEqual(660, company.json()['ratings'][0]['rating'])
