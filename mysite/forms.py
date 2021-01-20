from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"type": "email", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
