from django.db import models
import datetime


class Post(models.Model):
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=128)
    publishDate = models.DateField(auto_now_add=True, auto_now=False, editable=False)

