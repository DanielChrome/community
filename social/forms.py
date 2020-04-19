from django import forms
from users.models import CustomUser


class UserPostsForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'rows': 2}))


class UserProfile(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea', 'rows': 2}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'bio']
