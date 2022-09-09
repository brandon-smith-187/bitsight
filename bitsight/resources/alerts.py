from bitsight.resources.bitsight import BitSight, Endpoints


class Alerts(BitSight):
    v2_endpoint = f"{Endpoints.V2.alerts}"

    def __init__(self):
        super().__init__()

    def get_alerts(self, params=None, **kwargs):
        """
        Get all alerts
        :param params: filters for the request
        :return: json representation of all alerts
        """

        return self.get(endpoint=self.v2_endpoint, params=params, **kwargs)

    def get_latest_alerts(self, params=None, **kwargs):
        """
        Get the latest alerts
        :param params: filters for the request
        :return: json representation of the latest alerts
        """

        return self.get(endpoint=self.v2_endpoint + "latest", params=params, **kwargs)
