from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime


class UserPost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s' % self.message[0: 100]


class CommentPost(models.Model):
    post = models.ForeignKey(
        UserPost,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s' % self.message[0: 100]
