from django.urls import path, include
from social import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.main, name="main"),
    path("<str:user_name>", views.profile, name="profile"),
    path("<str:user_name>/addconnection", views.add_connection, name="addconnection"),
    path("<str:user_name>/removeconnection", views.remove_connection, name="removeconnection"),
    path("<str:user_name>/posts", views.user_post, name='userposts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
