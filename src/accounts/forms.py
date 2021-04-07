# from django.forms import modalForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
