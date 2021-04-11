# from django.forms import modalForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import EndUser, Contractor, AddressInfo


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
        model = Contractor
        fields = ['company_name']


class EndUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = EndUser
        fields = []


class AddressInfoForm(forms.ModelForm):
    class Meta:
        model = AddressInfo
        fields = '__all__'
