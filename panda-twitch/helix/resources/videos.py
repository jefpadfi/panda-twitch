from helix.api import HelixApi
from helix.decorators import oauth_or_app_access_required
import requests


class TwitchVideos(HelixApi):
    @oauth_or_app_access_required
    def get_videos(self, video_id: str = None, user_id: str = None, game_id: str = None, after: str = None,
                   before: str = None, first: str = "20", language: str = None, period: str = None, sort: str = None,
                   video_type: str = None):
        """
        Gets video information by video ID (one or more), user ID (one only), or game ID (one only)

        :param video_id: ID of the video being queried. Limit: 100. If this is specified, you cannot use any of the optional query parameters below.
        :param user_id: ID of the user who owns the video. Limit: 1
        :param game_id: ID of the game the video is of. Limit: 1
        :param after: Cursor for forward pagination: tells the server where to start fetching the next set of results.
        :param before: Cursor for backward pagination: tells the server where to start fetching the next set of results.
        :param first: Number of values to be returned when getting videos by user or game ID. Limit: 100 Default: 20
        :param language: Language of the video being queried. Limit 1
        :param period: Period during which the video was created. Valid values: all, day, week, month. Default: all
        :param sort: Sort order of the videos. Valid values: time, trending, view. Default:time
        :param video_type: Type of video. Valid values: all, upload, archive, highlight. Default: all
        :return: created_at, description, duration, id, language, pagination, published_at, thumbnail_url, title, type, url, user_id, user_name, view_count, viewable
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Client-Id": f"{self.client_id}",
        }

        params = {
            "id": video_id,
            "user_id": user_id,
            "game_id": game_id,
            "after": after,
            "before": before,
            "first": first,
            "language": language,
            "period": period,
            "sort": sort,
            "video_type": video_type
        }

        response = requests.get(f"{self.base_url}/videos", headers=headers, params=params)
        return response
