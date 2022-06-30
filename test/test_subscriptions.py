from unittest import TestCase

from bitsight.resources.subscriptions import Subscriptions


class TestSubscriptions(TestCase):
    subscriptions = Subscriptions()
    companies = [
        '1e1ece23-cf39-4f8a-92ea-ed8db0d55316',
        'af0bdaa7-6c2e-419f-975e-1ba220bd17f0',
        '5e7a17d5-9151-4648-b0c2-d1ff52e6dd52'
    ]

    def test_post_subscribe(self):
        for company in self.companies:
            response = self.subscriptions.post_subscribe(guid=company)
            print(response.json())
            self.assertEqual(200, response.status_code)

    def test_post_bulk_subscribe(self):
        response = self.subscriptions.post_bulk_subscribe(guids=self.companies)
        print(response.json())
        self.assertEqual(200, response.status_code)

    def test_delete_unsubscribe(self):
        for company in self.companies:
            response = self.subscriptions.delete_unsubscribe(guid=company)
            print(response.text)
            self.assertEqual(204, response.status_code)
