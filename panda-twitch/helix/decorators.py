from helix.exceptions import TwitchScopeMissingException, TwitchAuthenticationException
from helix.api import HelixApi


def oauth_required(func):
    def inner(self, *args, **kwargs):
        if self.token is None:
            raise TwitchAuthenticationException("An OAuth Token is required.")
        func(self)
    return inner


def app_access_required(func):
    def inner(self, *args, **kwargs):
        if self.token is None:
            raise TwitchAuthenticationException("An App Access Token is required.")
        func(self)
    return inner


def oauth_or_app_access_required(func):
    def inner(self, *args, **kwargs):
        if self.token is None:
            raise TwitchAuthenticationException("Either an OAuth or an App Access Token is required.")
        func(self)
    return inner


def required_scope(*args, **kwargs):
    def inner(func):
        if args[0] not in args[1]:
            raise TwitchScopeMissingException(f"You are missing the required scope for this function. "
                                              f"Scope Needed: {args[0]}")
        func()
    return inner
