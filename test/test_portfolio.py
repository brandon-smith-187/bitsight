from unittest import TestCase

from bitsight.resources.portfolio import Portfolio


class TestPortfolio(TestCase):
    portfolio = Portfolio()

    def test_get_folder(self):
        portfolio = self.portfolio.get_portfolio(folder='d87cf106-126e-4bbc-99f7-12ee0e069ff4')
        self.assertEqual(144, len(portfolio))

    def test_get_portfolio(self):
        portfolio = self.portfolio.get_portfolio()
        self.assertEqual(3707, len(portfolio))

    def test_small_folder(self):
        portfolio = self.portfolio.get_portfolio(folder='64b5f629-662d-490b-adbb-993ef3e9f697')
        self.assertEqual(15, len(portfolio))

    def test_get_infected_companies(self):
        portfolio = self.portfolio.get_infected_companies(infections='Trickbot')
        self.assertEqual(55, len(portfolio))

        portfolio = self.portfolio.get_infected_companies(infections='CrossRider')
        self.assertEqual(301, len(portfolio))

    def test_get_vulnerable_companies(self):
        portfolio = self.portfolio.get_vulnerable_companies(vulnerabilities='CVE-2022-31043')
        self.assertEqual(57, len(portfolio))
        portfolio = self.portfolio.get_vulnerable_companies(vulnerabilities='CVE-2022-30556')
        self.assertEqual(1170, len(portfolio))

    def test_get_portfolio_statics(self):
        portfolio = self.portfolio.get_portfolio_statics()
        self.assertEqual(200, portfolio.status_code)
        print(portfolio.json())
