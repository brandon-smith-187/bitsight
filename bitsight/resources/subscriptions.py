from bitsight.resources.bitsight import BitSight, Endpoints


class Subscriptions(BitSight):
    v1_endpoint = f"{Endpoints.V1.subscriptions}"

    def __init__(self):
        super().__init__()

    def post_subscribe(self, guid, license_type="continuous_monitoring", **kwargs):
        """
        Request to subscribe to a company in BitSight
        :param guid: the guid for the company to subscribe to
        :param license_type: the license to use for the subscription
        :return: response object with confirmation in the content
        """
        payload = {f"{license_type}": {"companies": [{"guid": guid}]}}

        return self.post(endpoint=self.v1_endpoint, json=payload, **kwargs).json()

    def post_bulk_subscribe(
            self,
            guids,
            license_type="continuous_monitoring",
            tier=None,
            folders=None,
            **kwargs,
    ):
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
            company_dict = {"guid": guid, "type": f"{license_type}"}
            if tier is not None:
                company_dict.update({"tier": tier})
            if folders is not None:
                company_dict.update({"folder": folders})

            sub_dict["add"].append(company_dict)
        payload = sub_dict
        response = self.post(endpoint=self.v1_endpoint + "bulk", json=payload, **kwargs)
        return response

    def delete_unsubscribe(self, guid, **kwargs):
        """
        Unsubscribe from a company in BitSight
        :param guid: the guid for the company to be unsubscribed from
        :return: response object with status code, text, etc.
        """
        return self.delete(endpoint=self.v1_endpoint + guid, **kwargs)

    def get_subscription_details(self, **kwargs):
        """
        Get subscriptions details
        :return: json representation of subscriptions details
        """
        return self.get(endpoint=self.v1_endpoint, **kwargs)

    def get_expired_subscriptions(self, **kwargs):
        """
        Get expired subscriptions details
        :return: json representation of expired subscriptions details
        """
        return self.get(endpoint=self.v1_endpoint + "expired", **kwargs)
