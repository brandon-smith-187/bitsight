from bitsight.api_io.request_handler import RequestHandler


class Subscriptions:
    V1_ENDPOINT = 'https://api.bitsighttech.com/ratings/v1/subscriptions/'

    def __init__(self):
        super().__init__()
        self.handler = RequestHandler()

    def post_subscribe(self, guid, license_type="continuous_monitoring", **kwargs):
        """
        Request to subscribe to a company in BitSight
        :param guid: the guid for the company to subscribe to
        :param license_type: the license to use for the subscription
        :return: response object with confirmation in the content
        """
        payload = {license_type: {"companies": [{"guid": guid}]}}

        return self.handler.post(self.V1_ENDPOINT, json=payload, **kwargs)

    def post_bulk_subscribe(self, guids, license_type="continuous_monitoring", tier=None, folders=None, **kwargs):
        """
        Request to subscribe to multiple companies in BitSight
        :param guids: list of guids to subscribe to
        :param license_type: the license to use for the subscriptions
        :param tier: the tier to add the companies to
        :param folders: the list of folders to add the company to
        :return: response object with confirmation in the content
        """
        sub_dict = {"add": []}
        for guid in guids:
            company_dict = {"guid": guid, "type": license_type}
            if tier is not None:
                company_dict.update({"tier": tier})
            if folders is not None:
                company_dict.update({"folder": folders})

            sub_dict["add"].append(company_dict)
        payload = sub_dict
        response = self.handler.post(self.V1_ENDPOINT + 'bulk', json=payload, **kwargs)
        return response

    def delete_unsubscribe(self, guid, **kwargs):
        """
        Unsubscribe from a company in BitSight
        :param guid: the guid for the company to be unsubscribed from
        :return: response object with status code, text, etc.
        """
        return self.handler.delete(request_url=self.V1_ENDPOINT + guid, **kwargs)
