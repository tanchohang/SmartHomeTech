# from django.forms import modalForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserDetail, AddressInfo


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']


class ContractorRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['company_name']


class HostRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['department', 'position']


class EndUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = []


class AddressInfoForm(forms.ModelForm):
    class Meta:
        model = AddressInfo
        fields = '__all__'
