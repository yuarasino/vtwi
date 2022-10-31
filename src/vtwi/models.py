from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property

from .api import get_twitter_profile, get_youtube_profile


class VTwiUser(AbstractUser):
    channel_id = models.SlugField(verbose_name="チャンネルID", blank=True, default="")

    class Meta:
        db_table = "vtwi_users"
        verbose_name = verbose_name_plural = "VTwiユーザー"

    @cached_property
    def twitter_profile(self):
        return get_twitter_profile(self)

    @cached_property
    def twitter_name(self):
        return self.twitter_profile[0]

    @cached_property
    def twitter_icon_url(self):
        return self.twitter_profile[1]

    @cached_property
    def youtube_profile(self):
        return get_youtube_profile(self)

    @cached_property
    def youtube_name(self):
        return self.youtube_profile[0]

    @cached_property
    def youtube_icon_url(self):
        return self.youtube_profile[1]
