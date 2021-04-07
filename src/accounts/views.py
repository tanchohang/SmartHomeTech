from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django import forms

from .forms import UserRegistrationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def home(request):
    return render(request, 'accounts/landing.html', {'include': True})


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


def products(request):
    return render(request, 'accounts/products.html')


def portfolio(request):
    return render(request, 'accounts/portfolio.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def about(request):
    return render(request, 'accounts/about.html')


def estimator(request):
    return render(request, 'accounts/estimator.html')


def registerPage(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            user = form.save()
            group = Group.objects.get(name='end-user')
            group.user_set.add(user)
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/dashboard')

    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register2.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('/login')
