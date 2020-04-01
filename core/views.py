from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from core.models import LogMessage
from django.views.generic import ListView
from social.views import main


def home(request):
    if request.user.is_authenticated:
        return main(request)
    else:
        return HttpResponseRedirect('/users/login')
