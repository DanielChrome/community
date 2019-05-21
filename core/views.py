import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.forms import LogMessageForm
from core.models import LogMessage
from django.views.generic import ListView


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def login(request):
    return render(request, 'core/login.html')


def contact(request):
    return render(request, "core/contact.html")


# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "core/log_message.html", {"form": form})
