from helix.api import HelixApi
from helix.decorators import oauth_or_app_access_required
import requests


class TwitchExtensions(HelixApi):
    @oauth_or_app_access_required
    def get_extension_transactions(self, extension_id: str, transaction_id: str = None, after: str = None,
                                   first: int = 20):
        """
        Gets extension transactions allows extension back end server to fetch a list of transactions that have occurred
        for their extension across all of Twitch.

        :param extension_id: ID of the extension to list transaction for. Maximum = 1
        :param transaction_id: Transaction IDs to loop up. Can include multiple to fetch multiple transaction in a single request.
        :param after: The cursor used to fetch the next page of data.
        :param first: Maximum number of objects to return. Default: 100 Default: 20
        :return: pagination, data, id, timestamp, broadcaster_id, broadcaster_name, user_id, user_name, product_type, product_data, domain, broadcast, expiration, sku, cost, amount, type, "bits", displayName, inDevelopment
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "extension_id": extension_id,
            "transaction_id": transaction_id,
            "after": after,
            "first": first
        }

        response = requests.get(f"{self.base_url}/extensions/transactions", headers=headers, params=params)
        return response
