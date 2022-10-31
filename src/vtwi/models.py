from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property

from . import api


class VTwiUser(AbstractUser):
    class Meta:
        db_table = "vtwi_users"
        verbose_name = verbose_name_plural = "VTwiユーザー"

    @cached_property
    def profile(self):
        return api.get_twitter_profile(self)

    @cached_property
    def screen_name(self):
        return self.profile[0]

    @cached_property
    def icon_url(self):
        return self.profile[1]
