from django.urls import path, include
from social import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.main, name="main"),
    path("profile", views.profile, name="profile"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
