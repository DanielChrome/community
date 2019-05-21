from django.urls import path
from core import views
from core.models import LogMessage
from django.conf import settings
from django.conf.urls.static import static


home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="core/index.html",
)


urlpatterns = [
    path("", home_list_view, name="home"),
    path("login", views.login, name="login"),
    path("contact", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
