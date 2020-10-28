from helix.api import HelixApi
from helix.decorators import oauth_required, oauth_or_app_access_required, required_scope, app_access_required
from helix.scopes import used_scopes, USER_EDIT_BROADCAST, CHANNEL_READ_STREAM_KEY
import requests


class TwitchStreams(HelixApi):
    @oauth_required
    @required_scope(CHANNEL_READ_STREAM_KEY, used_scopes)
    def get_stream_key(self, broadcaster_id):
        """
        Gets the channel stream key for a user.

        :param broadcaster_id: User ID of the broadcaster.
        :return: stream_key
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "broadcaster_id": broadcaster_id
        }

        response = requests.get(f"{self.base_url}/streams/key", headers=headers, params=params)
        return response

    @oauth_or_app_access_required
    def get_streams(self, after: str = None, before: str = None, first: int = 20, game_id: str = None,
                    language: str = None, user_id: str = None, user_login: str = None):
        """
        Gets information about active streams. Streams are returned sorted by number of current viewers, in descending
        order.

        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param before: Cursor for backward pagination: tells the server where to start fetching the next set of results.
        :param first: Maximum number of objects to return. Maximum:100 Default:20
        :param game_id: Returns streams broadcasting a specified game ID. You can specify up to 100 idS.
        :param language: Stream language. you can specify up to 100 languages.
        :param user_id: Returns streams broadcast by one or more specified user IDs. you can specify up to 100 ids.
        :param user_login: Returns streams broadcast by on or more specified user login names. You can specify up to 100 ids.
        :return: game_id, id, language, pagination, started_at, tag_ids,thumbnail_url, title, type, user_id, user_name,
        viewer_count
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}"
        }

        params = {
            "after": after,
            "before": before,
            "first": first,
            "game_id": game_id,
            "language": language,
            "user_id": user_id,
            "user_login": user_login
        }

        response = requests.get(f"{self.base_url}/streams", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(USER_EDIT_BROADCAST, used_scopes)
    def create_stream_marker(self, user_id: str, description: str = None):
        """
        Creates a marker in the stream of a user specified by the user ID. A marker is an arbitrary point in a stream
        the broadcaster wants to mark.

        :param user_id: ID of the broadcaster in whose live stream the marker is created.
        :param description: Description of or comments on the marker. Max length is 140 characters.
        :return: created_at, description, id, position_seconds
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
            "Content-Type": "application/json",
        }

        data = {
            "user_id": user_id,
            "description": description
        }

        response = requests.post(f"{self.base_url}/streams/markers", headers=headers, data=data)
        return response

    @oauth_required
    @required_scope(USER_EDIT_BROADCAST, used_scopes)
    def get_stream_markers(self, user_id: str, video_id: str, after: str = None, before: str = None, first: int = 20):
        """
        Gets a list of markers for either a specified user's most recent stream or specified VOD/video (stream).

        :param user_id: ID of the broadcaster from whose stream markers are returned.
        :param video_id: ID of the VOD/video show stream markers are returned.
        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param before: Cursor for backward pagination: tells the server where to start fetching the next set of results.
        :param first: Maximum number of objects to return. Maximum:100 Default:20
        :return: id, created_at, description, pagination, position_seconds, URL, user_id, user_name, video_id
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "user_id": user_id,
            "video_id": video_id,
            "after": after,
            "before": before,
            "first": first,
        }

        response = requests.get(f"{self.base_url}/streams/markers", headers=headers, params=params)
        return response

    @app_access_required
    def get_all_stream_tags(self, after: str = None, first: int = 20, tag_id: str = None):
        """
        Gets the list of all stream tags defined by Twitch, optionally filtered by tag ID(s).

        :param after: Cursor for forward pagination: tells the server where to start fetching the nest set of results.
        :param first: Maximum number of objects to return. Maximum: 100 Default: 20
        :param tag_id: ID of a tag. Multiple IDs can be specified, separated by ampersands. If provided, only the
        specified tag(s) is(are) returned.
        :return: id, is_auto, localization_names, localization_descriptions, pagination
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "after": after,
            "first": first,
            "tag_id": tag_id
        }

        response = requests.get(f"{self.base_url}/tags/streams", headers=headers, params=params)
        return response

    @app_access_required
    def get_stream_tags(self, broadcaster_id: str):
        """
        Gets the list of tags for specified stream (channel).

        :param broadcaster_id: ID of the stream that tags are going to be fetched.
        :return: is_auto, localization_names, localization_descriptions, tag_id
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "broadcaster_id": broadcaster_id
        }

        response = requests.get(f"{self.base_url}/streams/tags", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(USER_EDIT_BROADCAST, used_scopes)
    def replace_stream_tags(self, broadcaster_id: str, tag_ids: str = None):
        """
        Applies specified tags to a specified stream, overwriting any existing tags applied to that stream.

        :param broadcaster_id: ID of the stream for which tags are to be replaced.
        :param tag_ids: IDs of tags to be applied to the stream. Maximum of 100 supported.
        :return: Nothing is returned.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
            'Content-Type': 'application/json',
        }

        params = {
            "broadcaster_id": broadcaster_id,
        }

        data = {
            "tag_ids": tag_ids
        }

        response = requests.put(f"{self.base_url}/streams/tags", headers=headers, params=params, data=data)
        return response
