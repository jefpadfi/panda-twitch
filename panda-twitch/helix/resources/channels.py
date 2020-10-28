from helix.api import HelixApi
from helix.decorators import required_scope, oauth_or_app_access_required, oauth_required
from helix.scopes import used_scopes, CHANNEL_EDIT_COMMERCIAL, USER_READ_BROADCAST

import requests


class TwitchChannels(HelixApi):
    @required_scope(CHANNEL_EDIT_COMMERCIAL, used_scopes)
    def start_commercial(self, broadcaster_id: str, commercials_length: int):
        """
        Starts a commercial on a specified channel.

        :param broadcaster_id: ID of the channel requesting a commercial. Minimum: 1 Maximum: 1
        :param commercials_length: Desired length of the commercial in seconds. Valid options are 30, 60, 90, 120, 150,
        180
        :return: length of triggered commercial, message on why the request failed, and how long you may retry.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
            "Content-Type": 'application/json',
        }

        data = {
            "broadcaster_id": broadcaster_id,
            "length": commercials_length
        }

        response = requests.post(f"{self.base_url}/channels/commercial", headers=headers, data=data)
        return response

    @oauth_or_app_access_required
    def get_channel_information(self, broadcaster_id: str):
        """
        Gets Channel information for users.

        :param broadcaster_id: ID of the channel to be updated
        :return: broadcaster_id, game_name, game_id, broadcaster_language, title
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id,
        }

        response = requests.get(f"{self.base_url}/channels", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(USER_READ_BROADCAST, used_scopes)
    def modify_channel_information(self, broadcaster_id: str, game_id: str = None, broadcaster_language: str = None, title: str = None):
        """
        Modifies channel information for users.

        :param broadcaster_id: ID of the channel to be  updated.
        :param game_id: The Current game ID being played on the Channel.
        :param broadcaster_language: The language of the channel.
        :param title: The title of the stream.
        :return: HTTP Codes 204/400/500
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
            "Content-Type": "application/json",
        }

        params = {
            "broadcaster_id": broadcaster_id
        }

        data = {
            "game_id": game_id,
            "broadcaster_language": broadcaster_language,
            "title": title
        }

        response = requests.patch(f"{self.base_url}/channels", headers=headers, params=params, data=data)
        return response

