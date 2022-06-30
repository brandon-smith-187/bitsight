from unittest import TestCase

from bitsight.resources.companies import Companies


class TestCompanies(TestCase):
    companies = Companies()

    def test_get_findings(self):
        params = {'affects_rating': 'true'}
        findings = self.companies.get_findings(guid='97a6a734-b16f-47c2-a3c1-4f08358821a3', params=params)
        # print(findings)
        self.assertEqual(327, len(findings))
