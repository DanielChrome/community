from django.db import models
from django.conf import settings
from django.utils import timezone


class UserPost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    created_at = models.DateTimeField("created at")

    def __str__(self):
        return '%s' % self.message[0: 100]
