from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'accounts/landing.html', {'include': True})


def login(request):
    return render(request, 'accounts/login.html', {'include': False})

def register(request):
    return render(request, 'accounts/register.html', {'include': True})


def services(request):
    return render(request, 'accounts/services.html', {'include': True})

def portfolio(request):
    return render(request, 'accounts/portfolio.html', {'include': True})


def contact(request):
    return render(request, 'accounts/contact.html')


def about(request):
    return render(request, 'accounts/about.html')


def estimator(request):
    return render(request, 'accounts/estimator.html')
