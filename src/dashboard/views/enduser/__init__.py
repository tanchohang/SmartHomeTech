
from django.shortcuts import render

from .messages import *
from .quotes import *


def dashboard(request):
    return render(request, 'dashboard/user/overview.html')


def profile(request):
    return render(request, 'dashboard/user/profile.html', {'user': request.user})
