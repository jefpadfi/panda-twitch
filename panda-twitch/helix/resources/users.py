from helix.api import HelixApi
from helix.decorators import oauth_required, required_scope, oauth_or_app_access_required
from helix.scopes import used_scopes, USER_EDIT_FOLLOWS, USER_READ_EMAIL, USER_EDIT, USER_READ_BROADCAST, \
    USER_EDIT_BROADCAST
import requests


class TwitchUsers(HelixApi):
    @oauth_required
    @required_scope(USER_EDIT_FOLLOWS, used_scopes)
    def create_user_follows(self, from_id: str, to_id: str, allow_notifications: bool = False):
        """
        Adds a specified user to the followers of a specified channel.

        :param from_id: User ID of the follower.
        :param to_id: ID of the channel to be followed by the user
        :param allow_notifications: If true, the user gets email or push notifications when the channel goes live. Default: false
        :return: Codes 204/400/422
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
            "Content-Type": "application/json",
        }

        data = {
            "from_id": from_id,
            "to_id": to_id,
            "allow_notifications": allow_notifications
        }

        response = requests.post(f"{self.base_url}/users/follows", headers=headers, data=data)
        return response

    @oauth_required
    @required_scope(USER_EDIT_FOLLOWS, used_scopes)
    def delete_user_follows(self, from_id: str, to_id: str):
        """
        Deletes a specified user from the followers of a specified channel.

        :param from_id: User ID of the follower.
        :param to_id: Channel to be unfollowed by the user.
        :return: Codes 204/400/422
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "from_id": from_id,
            "to_id": to_id,
        }

        response = requests.delete(f"{self.base_url}users/follows", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(USER_READ_EMAIL, used_scopes)
    def get_users(self, user_id: str = None, login: str = None):
        """
        Gets information about one or more specified Twitch users. Users are identified by optional users IDs and/or
        login name. If neither a user ID nor a login name is specified, the user is looked up by Bearer Token.

        :param user_id: User ID. Multiple user IDs can be specified. Limit: 100
        :param login: User login name. Multiple login names can be specified. Limit: 100
        :return: broadcaster_type, description, display_name, email, id, login, offline_image_url, profile_image_url,
        type, view_count, created_at
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "id": user_id,
            "login": login
        }

        response = requests.get(f"{self.base_url}/users", headers=headers, params=params)
        return response

    @oauth_or_app_access_required
    def get_users_follows(self, after: str = None, first: int = 20, from_id: str = None, to_id: str = None):
        """
        Gets information on follow relationships between two Twitch Users. Information returned is sorted in order, most
         recent follow first.

        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param first: Maximum number of objects to return. maximum: 100 Default: 20
        :param from_id: User ID. The request returns information about users who are being followed by the from_id user.
        :param to_id: User ID. The request returns information about users who are following the to_id user.
        :return: followed_at, from_id, from_name, pagination, to_id, to_name, total
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "after": after,
            "first": first,
            "from_id": from_id,
            "to_id": to_id,
        }

        response = requests.get(f"{self.base_url}/users/follows", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(USER_EDIT, used_scopes)
    def update_user(self, description: str = None):
        """
        Updates teh description of a user specified by a Bearer token.

        :param description: User's account description.
        :return: broadcaster_type, description, display_name, email, id, login, offline_image_url, profile_image_url, type, view_count, created_at
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "description": description,
        }

        response = requests.put(f"{self.base_url}/helix/users", headers=headers, params=params)
        return response

    @oauth_required
    @required_scope(USER_READ_BROADCAST, used_scopes)
    def get_user_extensions(self):
        """
        Gets a list of all extensions (both active and inactive) for a specified user, identified by a Bearer token.

        :return: can_activate, id, name, type, version
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        response = requests.get(f"{self.base_url}/users/extensions/list", headers=headers)
        return response

    @oauth_required
    @required_scope(USER_EDIT_BROADCAST, used_scopes)
    def get_user_active_extensions(self, user_id: str = None):
        """
        Gets information about active extensions installed by a specified user, identified by a user ID or Bearer token.

        :param user_id: ID of the user whose installed extensions will be returned. Limit: 1
        :return: active, component, id, name, overlay, panel, version, x, y
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        response = requests.get(f"{self.base_url}/users/extensions", headers=headers)
        return response

    @oauth_required
    @required_scope(USER_EDIT_BROADCAST, used_scopes)
    def update_user_extensions(self):
        """
        Updates the activation state, extension ID, and/or version number of installed extensions for a specified user,
        identified by a Bearer token.

        :return: active, component, id, name, overlay, panel, version, x, y
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
            "Content-Type": "application/json",
        }

        # response = requests.put(f"{self.base_url}/users/extensions", headers=headers,)
        return "This API call is not supported right now."
