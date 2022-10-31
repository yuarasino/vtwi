from django.conf import settings
from requests import RequestException
from requests_oauthlib import OAuth1Session


def get_twitter_profile(user):
    if not hasattr(user, "social_auth"):
        return "", ""

    social_auth = user.social_auth.first()
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
        screen_name = data["screen_name"]
        icon_url = data["profile_image_url_https"]
    except RequestException:
        return "", ""
    return screen_name, icon_url
