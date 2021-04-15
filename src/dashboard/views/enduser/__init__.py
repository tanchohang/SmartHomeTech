
from django.shortcuts import render

from .messages import *
from .quotes import *

from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard/user/overview.html')


def profile(request):
    return render(request, 'dashboard/user/profile.html', {'user': request.user})
