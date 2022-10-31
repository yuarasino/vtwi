import requests
from django.conf import settings
from requests import RequestException
from requests_oauthlib import OAuth1Session


def get_twitter_profile(vtwi_user):
    if not hasattr(vtwi_user, "social_auth"):
        return "", ""
    social_auth = vtwi_user.social_auth.first()
    access_token = social_auth.extra_data["access_token"]
    twitter = OAuth1Session(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_KEY_SECRET,
        access_token["oauth_token"],
        access_token["oauth_token_secret"],
    )
    try:
        res = twitter.get(
            "https://api.twitter.com/1.1/users/show.json",
            params={
                "id": social_auth.uid,
            },
        )
        res.raise_for_status()
        data = res.json()
        name = data["name"]
        icon_url = data["profile_image_url_https"]
    except (RequestException, KeyError):
        return "", ""
    return name, icon_url


def get_youtube_profile(vtwi_user):
    if not vtwi_user.channel_id:
        return "", ""
    try:
        res = requests.get(
            "https://www.googleapis.com/youtube/v3/channels",
            params={
                "id": vtwi_user.channel_id,
                "part": "snippet",
                "key": settings.YOUTUBE_API_KEY,
            },
        )
        res.raise_for_status()
        data = res.json()
        name = data["items"][0]["snippet"]["title"]
        icon_url = data["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    except (RequestException, KeyError):
        return "", ""
    return name, icon_url


def exists_youtube_channel(channel_id):
    try:
        res = requests.get(
            "https://www.googleapis.com/youtube/v3/channels",
            params={
                "id": channel_id,
                "part": "snippet",
                "key": settings.YOUTUBE_API_KEY,
            },
        )
        res.raise_for_status()
        data = res.json()
        result = channel_id == data["items"][0]["id"]
    except (RequestException, KeyError):
        return False
    return result
