from django import forms
from users.models import CustomUser


class UserPostsForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'rows': 2}))


class UserProfile(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input', 'required': False}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input', 'required': False}))
    bio = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'textarea', 'rows': 2,'required': False}))
    photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'bio', 'photo']
