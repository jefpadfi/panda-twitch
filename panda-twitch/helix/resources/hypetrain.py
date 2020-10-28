from helix.api import HelixApi
from helix.decorators import oauth_or_app_access_required, required_scope
from helix.scopes import used_scopes, CHANNEL_READ_HYPE_TRAIN
import requests


class TwitchHypeTrain(HelixApi):
    @oauth_or_app_access_required
    @required_scope(CHANNEL_READ_HYPE_TRAIN, used_scopes)
    def get_hype_train_events(self, broadcaster_id: str, first: int = 1, event_id: str = None, cursor: str = None):
        """
        Gets the information of the most recent Hype Train of the Given channel ID> When there is currently an active
        Hype Train, it returns information about that Hype Train.

        :param broadcaster_id: User ID of the broadcaster. Must match the User ID in the Bearer token if User Token is Used.
        :param first: Maximum number of objects to return. Maximum: 100 Default: 1
        :param event_id: The id of the wanted event, if known.
        :param cursor: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :return: id, event_type, event_timestamp, version, event_data, id, broadcaster_id, started_at, expires_at, cooldown_end_time, level, goal, total, top_contributions, total, type, user, last_contribution, total, type, user, pagination
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "first": first,
            "id": event_id,
            "cursor": cursor
        }

        response = requests.get(f"{self.base_url}/hypetrain/events", headers=headers, params=params)
        return response
