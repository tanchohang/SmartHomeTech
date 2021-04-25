
from django.shortcuts import render

from .messages import *
from .quotes import *
from django.contrib.auth.decorators import login_required
from dashboard.decorators import allowed_users
from django.contrib.auth.models import User
from accounts.models import UserDetail
from dashboard.models import Project
from accounts.forms import AddressInfoForm

from dashboard.forms import ProjectForm, FileForm


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
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def projects(request):
    if request.user.groups.first().name == 'host':
        projects = Project.objects.all()
        contractors = User.objects.filter(groups__name='contractor')

        return render(request, 'dashboard/host/projects.html', {'projects': projects, 'contractors': contractors})
    else:
        if request.method == "POST":
            projectForm = ProjectForm(request.POST)
            addressForm = AddressInfoForm(request.POST)

            if projectForm.is_valid() and addressForm.is_valid():
                address = addressForm.save()
                project = projectForm.save(commit=False)
                project.owner = request.user.userdetail
                project.address = address
                project.save()

            return redirect('projects')
        else:
            projectForm = ProjectForm()
            addressForm = AddressInfoForm()
            appointmentForm = AppointmentForm()

            projects = Project.objects.filter(
                owner_id=request.user.userdetail.id)

            return render(request, 'dashboard/user/projects.html', {'projects': projects, 'projectForm': projectForm, 'addressForm': addressForm, 'appointmentForm': appointmentForm})


@login_required(login_url='login')
@allowed_users(allowed_groups=['contractor'])
def user_requests(request):
    # user = UserDetail.objects.get(user_id=request.user.id)
    # users = user.assigned.all()
    projects = Project.objects.filter(
        contractor=request.user.userdetail)
    return render(request, 'dashboard/user/user-requests.html', {'projects': projects})


@login_required(login_url='login')
@allowed_users(allowed_groups=['contractor'])
def user_requests_confirmation(request, project):

    project = Project.objects.get(id=project)
    project.contractor_confirmed = True
    project.save()
    return redirect('user-requests', {'navlink': 'user-requests'})
