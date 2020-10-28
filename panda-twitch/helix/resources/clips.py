from helix.api import HelixApi
from helix.decorators import oauth_required, required_scope
from helix.scopes import used_scopes, CLIPS_EDIT
import requests


class TwitchClips(HelixApi):
    @oauth_required
    @required_scope(CLIPS_EDIT, used_scopes)
    def create_clip(self, broadcaster_id: str, has_delay: bool = False):
        """
        Creates a cli programmatically. This returns both an ID and an edit URL for the new clip.

        :param broadcaster_id: Broadcaster ID of the stream from which the clip will be made.
        :param has_delay: If false, the clip is captured from the live stream when the API is called.
        :return: edit_url, id
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "has_delay": has_delay
        }

        response = requests.post(f"{self.base_url}/clips", headers=headers, params=params)
        return response

    def get_clips(self, broadcaster_id: str, game_id: str, clip_id: str, after: str = None, before: str = None, ended_at: str = None, first: int = 20, started_at: str = None):
        """
        Gets clip information by clip ID (one or more), broadcaster ID (one only), or game ID (one only). Clips are returned sorted by view count, in descending order.

        :param broadcaster_id: ID of the broadcaster for whom clips are returned.
        :param game_id: ID of the game for which clips are returned.
        :param clip_id:ID of the clip being queried. (Limit: 100).
        :param after: Cursor for forward pagination.
        :param before: Cursor for backward pagination.
        :param ended_at: Ending date/time for returned clips, in RFC3339 format.
        :param first:Maximum number of objects return. Maximum: 100, Default:20
        :param started_at: Starting date/time for returned clips, in RFC3339 format.
        :return: broadcaster_id, broadcaster_name, created_at, creator_id, creator_name, embed_url, game_id, id, language, pagination, thumbnail_url, title, url, video_id, view_count
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "game_id": game_id,
            "id": clip_id,
            "after": after,
            "before": before,
            "ended_at": ended_at,
            "first": first,
            "started_at": started_at
        }

        response = requests.get(f"{self.base_url}/clips", headers=headers, params=params)
        return response
