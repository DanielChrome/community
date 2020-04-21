from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class CustomUser(AbstractUser):
    bio = models.TextField(default="")
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)
    photo_small = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(64, 64)],
                                 format='JPEG',
                                 options={'quality': 80})
    photo_profile = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(200, 200)],
                                 format='JPEG',
                                 options={'quality': 80})
    # add additional fields in here

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ConnectionType(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class ConnectionSubtype(models.Model):
    type = models.ForeignKey(ConnectionType,  on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Connections(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='connections_user'
    )
    connection = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='connections_connect'
    )
    since = models.DateTimeField("since")
    connection_type = models.ForeignKey(
        ConnectionType,
        on_delete=models.CASCADE,
    )
    connection_subtype = models.ForeignKey(
        ConnectionSubtype,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    pendent = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name + " - " + self.connection.first_name + ": " + self.connection_type.description
