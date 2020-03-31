from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .forms import UserPostsForm
from .models import UserPost


def main(request):
    return render(request, "main.html")


def profile(request):
    return render(request, "profile.html")


def user_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserPostsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = UserPost()
            post.author = request.user
            post.message = form.cleaned_data['message']
            post.created_at = today = datetime.today()
            post.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/social/posts')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserPostsForm()

    return render(request, 'user_posts.html', {'form': form, 'posts': UserPost.objects.all()[:5]})
