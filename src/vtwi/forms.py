from django.forms import ModelForm, ValidationError

from .api import exists_youtube_channel
from .models import VTwiUser


class VTwiUserForm(ModelForm):
    class Meta:
        model = VTwiUser
        fields = ["channel_id"]

    def clean_channel_id(self):
        channel_id = self.cleaned_data.get("channel_id")
        if channel_id and not exists_youtube_channel(channel_id):
            raise ValidationError("チャンネルが存在しません。", code="invalid")
        return channel_id
