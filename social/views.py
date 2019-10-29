import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView


def main(request):
    return render(request, "main.html")
