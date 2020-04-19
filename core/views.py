from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from core.models import LogMessage
from django.views.generic import ListView


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/social')
    else:
        return HttpResponseRedirect('/users/login')
