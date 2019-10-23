import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import LogMessage
from django.views.generic import ListView


def home(request):
    return render(request, "core/home.html")

def login(request):
    return render(request, 'registration/login.html')


def contact(request):
    return render(request, "core/contact.html")

