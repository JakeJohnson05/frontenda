from django.forms import ModelForm
from . import models


class newPostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['subject', 'body', ]
