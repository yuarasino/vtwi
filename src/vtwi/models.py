from django.contrib.auth.models import AbstractUser


class VTwiUser(AbstractUser):
    class Meta:
        db_table = "vtwi_users"
        verbose_name = verbose_name_plural = "VTwiユーザー"
