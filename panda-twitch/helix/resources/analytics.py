from helix.api import HelixApi
from helix.scopes import used_scopes, ANALYTICS_READ_GAMES, ANALYTICS_READ_EXTENSIONS
from helix.decorators import oauth_required, required_scope

import requests


class TwitchAnalytics(HelixApi):
    @required_scope(ANALYTICS_READ_EXTENSIONS, used_scopes)
    def get_extension_analytics(self, after: str = None, ended_at: str = None, extension_id: str = None, first: int = 20,
                                started_at: str = None, analytics_type: str = None):
        """
        Gets a URL that extensions developers can use to download analytic reports (CSV Files) for their extensions.
        The URL is valid for 5 minutes.

        :param after: Cursor for forward pagination
        :param ended_at: Ending date/time for returned reports.
        :param extension_id: Client ID value assigned to the extension when it was created.
        :param first: Maximum number of objects to return. Maximum 100. Default 20.
        :param started_at: Starting date/time for returned reports in RFC3339 format.
        :param analytics_type: The type of analytics report that is returned.
        :return: ended_at, extension_id, pagination, started_at, type, url
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "after": after,
            "ended_at": ended_at,
            "extension_id": extension_id,
            "first": first,
            "started_at": started_at,
            "type": analytics_type
        }

        response = requests.get(f"{self.base_url}/analytics/extensions", headers=headers, params=params)

        return response

    @oauth_required
    @required_scope(ANALYTICS_READ_GAMES, used_scopes)
    def get_game_analytics(self, after: str = None, ended_at: str = None, first: int = None, game_id: str = None,
                           started_at: str = None, analytics_type: str = None):
        """
        Gets a URL that game developers can use to download analytic reports.

        :param after: Cursor for forward pagination
        :param ended_at: Ending date/time for returned reports.
        :param first: Maximum number of objects to return. Maximum 100. Default 20.
        :param game_id: Game ID. IF this is specified, the returned URL points to an analytics report for the specified game.
        :param started_at: Starting date/time for returned reports in RFC3339 format.
        :param analytics_type: The type of analytics report that is returned.
        :return: ended_at, game_id, pagination, started_at, type, URL
        """
        headers = {
            "Authorization": F"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "after": after,
            "ended_at": ended_at,
            "first": first,
            "game_id": game_id,
            "started_at": started_at,
            "type": analytics_type
        }

        response = requests.get(f"{self.base_url}/analytics/games", headers=headers, params=params)
        return response
