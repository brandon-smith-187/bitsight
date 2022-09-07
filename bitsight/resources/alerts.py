from bitsight.api_io.request_handler import RequestHandler


class Alerts:
    V2_ENDPOINT = "https://api.bitsighttech.com/v2/alerts/"

    def __init__(self):
        super().__init__()
        self.handler = RequestHandler()

    def get_alerts(self, params=None, **kwargs):
        """
        Get all alerts
        :param params: filters for the request
        :return: json representation of all alerts
        """

        return self.handler.get(request_url=self.V2_ENDPOINT, params=params, **kwargs)

    def get_latest_alerts(self, params=None, **kwargs):
        """
        Get latest alerts
        :param params: filters for the request
        :return: json representation of the latest alerts
        """

        return self.handler.get(request_url=self.V2_ENDPOINT + 'latest', params=params, **kwargs)
