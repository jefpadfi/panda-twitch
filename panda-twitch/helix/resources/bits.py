from helix.api import HelixApi
from helix.decorators import oauth_or_app_access_required, required_scope, oauth_required
from helix.scopes import used_scopes, BITS_READ
import requests


class TwitchBits(HelixApi):
    @oauth_or_app_access_required
    def get_cheermotes(self, broadcaster_id: str):
        """
        Retrieves the list of available Cheermotes, animated emotes to which viewers can assign Bits, to cheer in chat.
        Cheermotes returned ar available throughout Twitch, in all Bits-enabled channels.

        :param broadcaster_id: ID for the broadcaster who might own specialized Cheermotes.
        :return: tiers, min_bits, id, color, images, can_cheer, show_in_bits_card, type, order, last_updated, is_charitable,
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id
        }

        response = requests.get(f"{self.base_url}/bits/cheermotes", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(BITS_READ, used_scopes)
    def get_bits_leaderboard(self, count: int = None, period: str = None, started_at: str = None, user_id: str = None):
        """
        Gets a ranked list of Bits leaderboard information for an authorized broadcaster.

        :param count: Number of results to be returned. Max:100 Default:20
        :param period: Time period over which data is aggregated (PST Timezone)
        :param started_at: Timestamp for the period over which the returned date is aggregated.
        :param user_id: ID of the user whose results are returned; i.e., the person who paid for the bits.
        :return: ended_at, rank, score, started_at, total, user_id, user_name
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "count": count,
            "period": period,
            "started_at": started_at,
            "user_id": user_id
        }

        response = requests.get(f"{self.base_url}/bits/leaderboard", headers=headers, params=params)
        return response
