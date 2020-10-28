from helix.api import HelixApi
from helix.decorators import oauth_or_app_access_required
import requests


class TwitchSearch(HelixApi):
    @oauth_or_app_access_required
    def search_categories(self, query: str, first: int = 20, after: str = None):
        """
        Returns a list of games or categories that match the query via name either entirely or partially.

        :param query: URI encoded search query
        :param first: Maximum number of objects to return. Maximum: 100 Default: 20
        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :return: box_art_url, name, id
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "query": query,
            "first": first,
            "after": after
        }

        response = requests.get(f"{self.base_url}/search/categories", headers=headers, params=params)
        return response

    @oauth_or_app_access_required
    def search_channels(self, query: str, first: int = 20, after: str = None, live_only: bool = False,):
        """
        Returns a list of channels (users who have streamed within the past 6 months) that match the query via channel
        name or description either entirely or partially.

        :param query: URI encoded search query.
        :param first: Maximum number of objects to return. Maximum:100 Default:20
        :param after: Cursor for forward pagination: tells the server were to start fetching the next set of results.
        :param live_only: Filter results for live streams only. Default: False
        :return: game_id, id, display_name, broadcaster_language, title, thumbnail_url, is_live, started_at, tags_ids
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "query": query,
            "first": first,
            "after": after,
            "live_only": live_only
        }

        response = requests.get(f"{self.base_url}/search/channels", headers=headers, params=params)
        return response
