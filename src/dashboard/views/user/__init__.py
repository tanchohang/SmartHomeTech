
from django.shortcuts import render

from .messages import *
from .quotes import *
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_users
from django.contrib.auth.models import User
from accounts.models import UserDetail


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def dashboard(request):
    return render(request, 'dashboard/user/overview.html')


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'dashboard/user/profile.html', {'user': user})


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor'])
def projects(request):
    return render(request, 'dashboard/user/projects.html')


@login_required(login_url='login')
@allowed_users(allowed_groups=['contractor'])
def user_requests(request):
    # user = UserDetail.objects.get(user_id=request.user.id)
    # users = user.assigned.all()
    users = UserDetail.objects.filter(
        contractor_id=request.user.userdetail)
    return render(request, 'dashboard/user/user-requests.html', {'users': users})


@login_required(login_url='login')
@allowed_users(allowed_groups=['contractor'])
def user_requests_confirmation(request, user):

    user = UserDetail.objects.get(id=user)
    user.contractor_confirmed = True
    user.save()
    print(user.contractor_confirmed)
    users = UserDetail.objects.filter(
        contractor_id=request.user.userdetail)
    return redirect('user-requests')
