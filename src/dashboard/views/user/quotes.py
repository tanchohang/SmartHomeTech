from django.shortcuts import render, redirect
from dashboard.models import Message, Quote, Project
from dashboard.forms import ProjectForm, QuotesForm, AppointmentForm
from accounts.forms import AddressInfoForm
from dashboard.decorators import allowed_users
from django.contrib.auth.decorators import login_required
import ast


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def quotes(request):
    if request.user.groups.first().name == 'host':
        projects = Project.objects.all()
        return render(request, 'dashboard/host/quotes.html', {'projects': projects})
    else:
        if request.method == 'POST':
            quoteForm = QuotesForm(request.POST)

            body = {
                'bedrooms': request.POST['bedrooms'],
                'system_required': request.POST['system_required'],
                'system_control': request.POST['system_control'],
                'description': request.POST['description']
            }
            quoteInstance = quoteForm.save(commit=False)
            quoteInstance.description = body
            quoteInstance.save()

            # Save Project
            project = Project.objects.get(id=request.POST['project'])
            project.quote = quoteInstance
            project.save()

            message = Message(creator=request.user.userdetail,
                              body=body, subject=project.name, project=project)

            message.save()

            return redirect('message')
        else:
            projectForm = ProjectForm()
            addressForm = AddressInfoForm()
            appointmentForm = AppointmentForm()

            projects = Project.objects.filter(
                owner=request.user.userdetail).filter(quote__isnull=True)

            return render(request, 'dashboard/user/quotes.html', {'projects': projects, 'projectForm': projectForm, 'addressForm': addressForm})


@login_required(login_url='login')
@allowed_users(allowed_groups=['host', 'end-user', 'contractor'])
def quotation(request, quote):
    if request.user.groups.first().name == 'host':
        if request.method == 'POST':
            quote = Quote.objects.get(id=quote)
            quote.quotation = request.POST['quotation']
            quote.save()
            return redirect('quotes')
    else:
        if request.method == 'POST':
            quote = Quote.objects.get(id=quote)
            quote.is_confirmed = True
            quote.save()
            return redirect('projects')
