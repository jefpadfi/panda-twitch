from helix.api import HelixApi
from helix.decorators import app_access_required, oauth_required
from helix.scopes import used_scopes
import requests


class TwitchEntitlements(HelixApi):
    @app_access_required
    def create_entitlement_grants_upload_url(self, manifest_id: str, entitlement_type: str):
        """
        Creates a URL where you can upload a manifest file and notify users that they have an entitlement.

        :param manifest_id: Unique identifier of the manifest file to be uploaded. Must be 1-64 characters.
        :param entitlement_type: Type of an entitlement being granted. Only bulk_drops_grant is supported.
        :return:
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "manifest_id": manifest_id,
            "type": entitlement_type
        }

        response = requests.post(f"{self.base_url}/entitlements/upload", headers=headers, params=params)
        return response

    def get_code_status(self, code: str, user_id: int):
        """
        Gets the status of one more provided codes. This API requires that the caller is an authenticated Twitch User.

        :param code: The code to get the status of.
        :param user_id: Represents anumeric Twitch user ID. The user account which is going to receive the entitlement.
        :return: data array with code and status.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "code": code,
            "user_id": user_id,
        }

        response = requests.get(f"{self.base_url}/entitlements/codes", headers=headers, params=params)
        return response

    @oauth_required
    def get_drops_entitlements(self, entitlement_id: str = None, user_id: str = None, game_id: str = None, after: str = None, first: int = 20):
        """
        Gets a list of entitlements for a given organization that have been granted to a game, user or both.

        :param entitlement_id: Unique identifier of the entitlement.
        :param user_id: A Twitch User ID
        :param game_id: A Twitch Game ID
        :param after: The cursor used to fetch the next page of data.
        :param first: Maximum number of entitlements to return. Default:20 Maximum:100
        :return: pagination, data, id, benefit_id, timestamp, user_id, game_id
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "entitlement_id": entitlement_id,
            "user_id": user_id,
            "game_id": game_id,
            "after": after,
            "first": first
        }

        response = requests.get(f"{self.base_url}/entitlements/drops", headers=headers, params=params)
        return response

    @app_access_required
    def redeem_code(self, code: str, user_id: int):
        """
        Redeems one or more provided codes to the authenticated Twitch user.
        This API requires that the caller is an authenticated Twitch User.

        :param code: The code to redeem to the authenticated user's account.
        :param user_id: Represents a numeric Twitch user ID. The user account which is going to receive the entitlement.
        :return: Array of payloads each of which includes code(string) and status (string)
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "code": code,
            "user_id": user_id
        }

        response = requests.post(f"{self.base_url}/entitlements/codes", headers=headers, params=params)
        return response
