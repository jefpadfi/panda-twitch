from helix.api import HelixApi
from helix.decorators import oauth_required, required_scope
from helix.scopes import used_scopes, CHANNEL_READ_SUBSCRIPTIONS
import requests


class TwitchSubscriptions(HelixApi):
    @oauth_required
    @required_scope(CHANNEL_READ_SUBSCRIPTIONS, used_scopes)
    def get_broadcaster_subscriptions(self, broadcaster_id: str, user_id: str = None):
        """
        Get all of a broadcaster's subscriptions.

        :param broadcaster_id: User ID of the broadcaster. Must match the USER id in the Bearer token.
        :param user_id: Returns broadcaster's subscribers. Unique identifier of account to get subscription status of. Accepts up to 100 values.
        :return: broadcaster_id, broadcaster_name, is_gift, tier, plan_name, user_id, user_name
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "user_id": user_id
        }

        response = requests.get(f"{self.base_url}/subscriptions", headers=headers, params=params)
        return response
