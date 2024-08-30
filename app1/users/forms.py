from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    # username = forms.CharField(
    #     label = "User name",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   "placeholder": "Enter username",
    #                                   "name": "username"})
    # )
    # password = forms.CharField(
    #     label="Password",
    #     widget=forms.PasswordInput(attrs={"autofocus": "current-password",
    #                                  "placeholder": "Enter password",
    #                                  "name": "password"})
    # )