from django.shortcuts import render

from .auth import *

# Create your views here.


def home(request):
    return render(request, 'accounts/landing.html', {'include': True, 'navlink': 'home'})


def services(request):
    return render(request, 'accounts/services.html', {'include': True, 'navlink': 'services'})


def portfolio(request):
    return render(request, 'accounts/portfolio.html', {'include': True, 'navlink': 'portfolio'})


def contact(request):
    return render(request, 'accounts/contact.html')


def about(request):
    return render(request, 'accounts/about.html',{'include': True, 'navlink': 'about'})


def estimator(request):
    return render(request, 'accounts/estimator.html')
