class PandaTwitchException(Exception):
    pass


class TwitchScopeMissingException(PandaTwitchException):
    pass


class TwitchAuthenticationException(PandaTwitchException):
    pass


class TwitchInternalServerException(PandaTwitchException):
    pass


class TwitchBadRequestException(PandaTwitchException):
    pass


class TwitchRateLimitException(PandaTwitchException):
    pass


class TwitchServiceUnavailableException(PandaTwitchException):
    pass


class TwitchMissingQueryParameter(PandaTwitchException):
    pass


class TwitchEntityException(PandaTwitchException):
    pass
