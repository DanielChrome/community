from django.contrib import admin
from .models import UserPost, CommentPost

# Register your models here.
admin.site.register(UserPost)
admin.site.register(CommentPost)
