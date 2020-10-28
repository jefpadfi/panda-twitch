from helix.api import HelixApi
from helix.decorators import app_access_required
import requests


class TwitchWebHooks(HelixApi):
    @app_access_required
    def get_webhook_subscriptions(self, after: str = None, first: str = "20"):
        """
        Gets the webhook subscriptions of a user identified by a Bearer token, in order of expiration.
        :param after: Cursor for forward pagination: tells the server where to started fetching the next set of results.
        :param first: Number of values to be returned per page. Limit: 100 Default: 20
        :return: callback, expires_at, pagination, topic, total.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "first": first,
            "after": after,
        }

        response = requests.get(f"{self.base_url}/webhooks/subscriptions", headers=headers, params=params)
        return response
