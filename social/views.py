from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView
from .forms import UserPostsForm
from .models import UserPost
from users.models import CustomUser, Connections


def main(request):
    connections = Connections.objects.filter(user=request.user)
    return render(request, "main.html", {'connections': connections})


def profile__(request):
    user_profile = request.user
    connections = Connections.objects.filter(user=request.user)
    return render(request, "profile.html", {'user_profile': user_profile, 'connections': connections})


def profile(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    connections = Connections.objects.filter(user=user_profile)
    return render(request, "profile.html", {'user_profile': user_profile, 'connections': connections})


def user_post(request, user_name):
    # if this is a POST request we need to process the form data
    try:
        user = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

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
            return HttpResponseRedirect('/social/' + user.username + '/posts')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserPostsForm()

    return render(request, 'user_posts.html', {'form': form, 'posts': UserPost.objects.filter(author=user)[:5],
                  'user_profile': user})
