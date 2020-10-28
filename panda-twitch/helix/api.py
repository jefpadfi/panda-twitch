import requests
import json


class HelixApi(object):
    def __init__(self, client_id, secret_id, token=None):
        # sets the base url for the api
        self.base_url = "https://api.twitch.tv/helix"
        # set the applications client_id
        self.client_id = client_id
        # set the application secrete id.
        self.secret_id = secret_id
        # Set the oauth token if it is already in out config file.
        self.token = token

    def get_oauth_token(self, scope_list=None):
        """
        Generate OAuth token for twitch.

        :return: OAuth token to the app. It is saved into the Applications config file.
        """
        params = {
            "client_id": self.client_id,
            "client_secret": self.secret_id,
            "grant_type": "client_credentials",
            "scope": scope_list
        }

        oauth_response = requests.post("https://id.twitch.tv/oauth2/token", params)
        jd = json.loads(oauth_response.text)
        self.token = jd["access_token"]
        return self.token

    def revoke_oauth_token(self, current_oauth):
        """
        Revoke Access Token

        :param current_oauth: token we will revoke
        :return: None
        """

        params = {
            "client_id": self.client_id,
            "token": current_oauth
        }
        
        revoke = requests.post("https://id.twitch.tv/oauth2/revoke", params=params)

    def generate_new_token(self, current_oauth):
        """
        Generates new OAuth token after it expires after 60 days.

        :param current_oauth: OAuth token to refresh.
        :return: New OAuth token.
        """
        # TODO: Should the main app check the days or should we store information via this library?
        pass
