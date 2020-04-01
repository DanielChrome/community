from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        # fields = ('username', 'email', 'bio')


class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input'}))
