from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(default="")
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)
    # add additional fields in here

    def __str__(self):
        return self.first_name + ' ' + self.last_name
