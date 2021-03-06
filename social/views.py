from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import ListView
from .forms import UserPostsForm, UserProfile
from .models import UserPost
from users.models import CustomUser, Connections, ConnectionType
from django.core.paginator import Paginator
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["followings"] = Connections.objects.filter(user=self.request.user, pendent=False)
        context["followers"] = Connections.objects.filter(connection=self.request.user, pendent=False)
        return context


@login_required
def profile(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    followings = Connections.objects.filter(user=user_profile, pendent=False)
    followers = Connections.objects.filter(connection=user_profile, pendent=False)
    followers_p = Connections.objects.filter(connection=user_profile, pendent=True)

    is_followed = False
    if(user_profile.username != request.user.username):
        try:
            is_followed = Connections.objects.get(user=request.user, connection=user_profile)
        except Connections.DoesNotExist:
            is_followed = False
        form = UserProfile(instance=user_profile)
    else:
        if request.method == 'POST':
            if 'photo_sub' in request.POST:
                form = UserProfile(request.POST, request.FILES)
                if form.is_valid():
                    user_profile.photo = form.cleaned_data['photo']
                    user_profile.save()
            elif 'info_sub' in request.POST:
                form = UserProfile(request.POST)
                # check whether it's valid:
                if form.is_valid():
                    user_profile.first_name = form.cleaned_data['first_name']
                    user_profile.last_name = form.cleaned_data['last_name']
                    user_profile.bio = form.cleaned_data['bio']
                    user_profile.save()

        # if a GET (or any other method) we'll create form
        else:
            form = UserProfile(instance=user_profile)

    data = {'user_profile': user_profile,
            'followings': followings,
            'followers': followers,
            'followers_p': followers_p,
            'is_followed': is_followed,
            'form': form}
    return render(request, "profile.html", data)


@login_required
def add_connection(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    is_friends = (len(Connections.objects.filter(user=request.user, connection=user_profile))) > 0

    if(not is_friends):
        connection = Connections()
        connection.user = request.user
        connection.connection = user_profile
        connection.connection_type = ConnectionType.objects.get(pk=1)  # Amigo
        connection.since = today = datetime.today()
        connection.save()

    return profile(request, user_name)


@login_required
def accept_connection(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    try:
        connect = Connections.objects.get(user=user_profile, connection=request.user)
    except Connections.DoesNotExist:
        raise Http404("Solicitação não encontrado")

    accept = (request.GET.get('accept', 'false'))

    if(accept == 'true'):
        connect.pendent = False
        connect.since = today = datetime.today()
        connect.save()
    else:
        connect.delete()

    return profile(request, request.user.username)


@login_required
def remove_connection(request, user_name):
    try:
        user_profile = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        raise Http404("Usuário não encontrado")

    Connections.objects.filter(user=request.user, connection=user_profile).delete()
    return profile(request, user_name)


@login_required
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
