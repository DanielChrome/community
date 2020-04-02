from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView
from .forms import UserPostsForm
from .models import UserPost
from users.models import CustomUser, Connections, ConnectionType
from django.core.paginator import Paginator


def main(request):
    connections = all_connections(request.user)
    return render(request, "main.html", {'connections': connections})


def profile(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    connections = all_connections(user_profile)

    is_friends = False
    if(user_profile.username != request.user.username):
        is_friends = (len(Connections.objects.filter(user=user_profile, connection=request.user)) +
                      len(Connections.objects.filter(user=request.user, connection=user_profile))) > 0

    data = {'user_profile': user_profile,
            'connections': connections,
            'is_friends': is_friends}
    return render(request, "profile.html", data)


def add_connection(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    is_friends = (len(Connections.objects.filter(user=user_profile, connection=request.user)) +
                  len(Connections.objects.filter(user=request.user, connection=user_profile))) > 0

    if(not is_friends):
        connection = Connections()
        connection.user = request.user
        connection.connection = user_profile
        connection.connection_type = ConnectionType.objects.get(pk=2)  # Amigo
        connection.since = today = datetime.today()
        connection.save()

    return profile(request, user_name)


def remove_connection(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")
    Connections.objects.filter(user=user_profile, connection=request.user).delete()
    Connections.objects.filter(user=request.user, connection=user_profile).delete()
    return profile(request, user_name)


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

    posts = UserPost.objects.filter(author=user).order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user_posts.html', {'form': form, 'posts': page_obj, 'user_profile': user})


def all_connections(user):
    list = []
    connections = Connections.objects.filter(user=user)
    for con in connections:
        list.append(con)
    connections = Connections.objects.filter(connection=user)
    for con in connections:
        con.connection = con.user
        con.user = user
        list.append(con)

    return list
