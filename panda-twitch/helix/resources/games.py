from helix.api import HelixApi
import requests


class TwitchGames(HelixApi):
    def get_top_games(self, after: str = None, before: str = None, first: int = 20):
        """
        Get Games sorted by number of current viewers on Twitch, most popular first.

        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param before: Cursor for backward pagination: tells the server where to start fetching the next results.
        :param first: Maximum number of objects to return. Default: 20 Maximum: 100
        :return: box_art_url, id, name, pagination
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "after": after,
            "before": before,
            "first": first
        }

        response = requests.get(f"{self.base_url}/games/top", headers=headers, params=params)
        return response

    def get_games(self, game_id: str, name: str):
        """
        Gets game information by the game ID or name

        :param game_id: Game ID. At most 100 id values can be specified.
        :param name: Game name. The name must be an exact match.
        :return: box_art_url, id, name
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "id": game_id,
            "name": name
        }

        response = requests.get(f"{self.base_url}/games", headers=headers, params=params)
        return response
