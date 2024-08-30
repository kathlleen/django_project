from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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


class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2'
                  ]


