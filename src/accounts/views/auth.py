from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django import forms

from ..forms import UserRegistrationForm, UserDetailForm, ContractorRegistrationForm, AddressInfoForm, contactDetailForm

from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from dashboard.decorators import unauthenticated_user


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,
                            password=password)
        login(request, user)
        return redirect('/login')
    else:
        return render(request, 'accounts/login.html')


@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        userdetailForm = UserDetailForm(request.POST)
        addressForm = AddressInfoForm(request.POST)
        contactForm = contactDetailForm(request.POST)
        if userForm.is_valid() and userdetailForm.is_valid() and addressForm.is_valid() and contactForm.is_valid():
            # save user
            user = userForm.save()
            # adpad user to end-user group
            group = Group.objects.get(name='end-user')
            group.user_set.add(user)

            # save address
            address = addressForm.save()

            # save contact
            contact = contactForm.save()

            # connect user to end-user and address table

            userdetail = userdetailForm.save(False)
            userdetail.user = user

            userdetail.address = address
            userdetail.contact = contact
            userdetail.save()

            # authenticate user
            authUser = authenticate(
                username=userForm.cleaned_data['username'], password=userForm.cleaned_data['password1'])

            # login user
            login(request, authUser)
            return HttpResponseRedirect('/login')

    else:
        userForm = UserRegistrationForm()
        userdetailForm = UserDetailForm()
        addressForm = AddressInfoForm()
        contactForm = contactDetailForm()

        return render(request, 'accounts/register2.html', {'userForm': UserRegistrationForm, 'userdetailForm': UserDetailForm, 'addressForm': AddressInfoForm, 'contactForm': contactForm})


def contractorRegisterPage(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        contractorForm = ContractorRegistrationForm(request.POST)
        addressForm = AddressInfoForm(request.POST)
        contactForm = contactDetailForm(request.POST)

        if userForm.is_valid() and contractorForm.is_valid() and addressForm.is_valid() and contactForm.is_valid():
            # save user
            user = userForm.save()
            # add user to contractor group
            group = Group.objects.get(name='contractor')
            group.user_set.add(user)

            # save address
            address = addressForm.save()

            # save contact
            contact = contactForm.save()

            # connect user to contractor and address table
            contractorUser = contractorForm.save(False)
            contractorUser.user = user
            contractorUser.address = address
            contractorUser.contact = contact

            contractorUser.save()

            # authenticate user
            authUser = authenticate(
                username=userForm.cleaned_data['username'], password=userForm.cleaned_data['password1'])

            # login user
            login(request, authUser)
            return HttpResponseRedirect('/login')

    else:
        userForm = UserRegistrationForm()
        contractorForm = ContractorRegistrationForm()
        addressForm = AddressInfoForm()
        contactForm = contactDetailForm()

        return render(request, 'accounts/register-contractor.html', {'userForm': UserRegistrationForm, 'contractorForm': ContractorRegistrationForm, 'addressForm': AddressInfoForm, 'contactForm': contactForm})


def logoutUser(request):
    logout(request)
    return redirect('/login')
