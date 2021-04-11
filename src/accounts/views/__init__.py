from django.shortcuts import render

from .auth import *

# Create your views here.


def home(request):
    return render(request, 'accounts/landing.html', {'include': True})


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
