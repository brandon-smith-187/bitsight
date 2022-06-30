from unittest import TestCase

from bitsight.resources.portfolio import Portfolio


class TestPortfolio(TestCase):
    portfolio = Portfolio()

    def test_get_folder(self):
        portfolio = self.portfolio.get_portfolio(folder='d87cf106-126e-4bbc-99f7-12ee0e069ff4')
        self.assertEqual(144, len(portfolio))

    def test_get_portfolio(self):
        portfolio = self.portfolio.get_portfolio()
        self.assertEqual(3693, len(portfolio))
