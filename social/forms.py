from django import forms


class UserPostsForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'rows': 2}))
