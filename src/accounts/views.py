from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'accounts/landing.html')


def login(request):
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
