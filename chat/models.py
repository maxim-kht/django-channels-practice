from django.contrib.auth.models import User
from django.db import models


class ChatMessage(models.Model):
    message = models.CharField(max_length=255, blank=True)
    room = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add=True)
