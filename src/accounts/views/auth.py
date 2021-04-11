from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django import forms

from ..forms import UserRegistrationForm, EndUserRegistrationForm, ContractorRegistrationForm, AddressInfoForm

from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
    else:
        return render(request, 'accounts/login.html')


def registerPage(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        endUserForm = EndUserRegistrationForm(request.POST)
        addressForm = AddressInfoForm(request.POST)
        print(addressForm.is_valid())
        if userForm.is_valid() and endUserForm.is_valid() and addressForm.is_valid():
            # save user
            user = userForm.save()
            # adpad user to end-user group
            group = Group.objects.get(name='end-user')
            group.user_set.add(user)

            # save address
            address = addressForm.save()

            # connect user to end-user and address table

            enduser = endUserForm.save(False)
            enduser.user = user

            enduser.address = address
            enduser.save()

            # authenticate user
            authUser = authenticate(
                username=userForm.cleaned_data['username'], password=userForm.cleaned_data['password1'])

            # login user
            login(request, authUser)
            return HttpResponseRedirect('/user/')

    else:
        userForm = UserRegistrationForm()
        endUserForm = EndUserRegistrationForm()
        addressForm = AddressInfoForm()

        return render(request, 'accounts/register2.html', {'userForm': UserRegistrationForm, 'endUserForm': EndUserRegistrationForm, 'addressForm': AddressInfoForm})


def contractorRegisterPage(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        contractorForm = ContractorRegistrationForm(request.POST)
        addressForm = AddressInfoForm(request.POST)
        print(addressForm.is_valid())
        if userForm.is_valid() and contractorForm.is_valid() and addressForm.is_valid():
            # save user
            user = userForm.save()
            # add user to contractor group
            group = Group.objects.get(name='contractor')
            group.user_set.add(user)

            # save address
            address = addressForm.save()

            # connect user to contractor and address table
            contractorUser = contractorForm.save(False)
            contractorUser.user = user
            contractorUser.address = address
            contractorUser.save()

            # authenticate user
            authUser = authenticate(
                username=userForm.cleaned_data['username'], password=userForm.cleaned_data['password1'])

            # login user
            login(request, authUser)
            return HttpResponseRedirect('/contractor/')

    else:
        userForm = UserRegistrationForm()
        contractorForm = ContractorRegistrationForm()
        addressForm = AddressInfoForm()

        return render(request, 'accounts/register-contractor.html', {'userForm': UserRegistrationForm, 'contractorForm': ContractorRegistrationForm, 'addressForm': AddressInfoForm})


def logoutUser(request):
    logout(request)
    return redirect('/login')
