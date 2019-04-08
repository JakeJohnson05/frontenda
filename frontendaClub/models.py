from django.db import models
from django.core.validators import MaxLengthValidator
import datetime


class Post(models.Model):
    subject = models.CharField(max_length=25)
    body = models.TextField(max_length=400, validators=[MaxLengthValidator(400)])
    publishDate = models.DateField(auto_now_add=True, auto_now=False, editable=False)

    def __str__(self):
      return self.subject
