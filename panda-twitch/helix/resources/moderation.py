from helix.api import HelixApi
from helix.decorators import oauth_required, required_scope
from helix.scopes import used_scopes, MODERATION_READ
import requests


class TwitchModeration(HelixApi):
    @oauth_required
    @required_scope(MODERATION_READ, used_scopes)
    def check_automod_status(self, broadcaster_id: str, msg_id: str, msg_text: str, user_id: str):
        """
        Determines whether a string message meets the channel's Automod requirements.

        :param broadcaster_id: Provided broadcaster_id must match the user_id in the auth token.
        :param msg_id: Developer-generated identifier for mapping messages to results.
        :param msg_text: Message text.
        :param user_id: User id of the sender.
        :return: msg_id, is_permitted
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }
        data = {
            "broadcaster_id": broadcaster_id,
            "msg_id": msg_id,
            "msg_text": msg_text,
            "user_id": user_id
        }
        response = requests.post(f"{self.base_url}/moderation/enforcements/status", headers=headers, data=data)
        return response

    @oauth_required
    @required_scope(MODERATION_READ, used_scopes)
    def get_banned_users(self, broadcaster_id: str, user_id: str = None, after: str = None, before: str = None):
        """
        Returns all banned and timed-out users in a channel.

        :param broadcaster_id: Provided broadcaster_id must match the user_id in the auth token.
        :param user_id: Filters the results and only returns a status objects for user who are banned in this channel and have a matching user_id.
        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param before: Cursor for backward pagination: tells the server where to start fetching the next set of results.
        :return: user_id, user_name, expires_as, pagination
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "user_id": user_id,
            "after": after,
            "before": before
        }

        response = requests.get(f"{self.base_url}/moderation/banned", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(MODERATION_READ, used_scopes)
    def get_banned_events(self, broadcaster_id: str, user_id: str = None, after: str = None, first: str = "20"):
        """
        Returns all user bans and un-bans in a channel.

        :param broadcaster_id: Provided broadcaster_id must match the user_id in the auth token.
        :param user_id: Filters the results and only returns a status object for users who are banned in this channel and have a matching user_id
        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param first: Maximum number of objects to return. Maximum:100 Default:20
        :return: id, event_type, event_timestamp, pagination, version, event_data
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "user_id": user_id,
            "after": after,
            "first": first
        }

        response = requests.get(f"{self.base_url}/moderation/banned/events", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(MODERATION_READ, used_scopes)
    def get_moderators(self, broadcaster_id: str, user_id: str = None, after: str = None):
        """
        Returns all moderators in a channel
        :param broadcaster_id: Provided broadcaster_id must match the user_id in the auth token.

        :param user_id: Filters the results and only returns a status object for users who are banned in this channel and have a matching user_id
        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :return: user_id, user_name, pagination
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "user_id": user_id,
            "after": after
        }

        response = requests.get(f"{self.base_url}/moderation/moderators", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(MODERATION_READ, used_scopes)
    def get_moderator_events(self, broadcaster_id: str, user_id: str = None):
        """
        Returns a list of moderators or users added and removed as moderators from a channel.

        :param broadcaster_id: Provided broadcaster_id must match the user_id in the auth token.
        :param user_id: Filters the results and only returns a status object for users who are banned in this channel and have a matching user_id
        :return: id, event_type, event_timestamp, pagination, version
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "broadcaster_id": broadcaster_id,
            "user_id": user_id
        }

        response = requests.get(f"{self.base_url}/moderation/moderators/events", headers=headers, params=params)
        return response
