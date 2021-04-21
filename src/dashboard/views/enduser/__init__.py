
from django.shortcuts import render

from .messages import *
from .quotes import *
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def dashboard(request):
    return render(request, 'dashboard/user/overview.html')


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def profile(request, username):
    return render(request, 'dashboard/user/profile.html', {'user': request.user})
