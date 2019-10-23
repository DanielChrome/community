from django.urls import path, include
from core import views
from core.models import LogMessage
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # path("logout", auth_views.LogoutView, name="logout"),
    path("admin/", admin.site.urls, name="admin"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
