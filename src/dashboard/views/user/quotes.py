from django.shortcuts import render, redirect
from dashboard.forms import QuotesForm
from dashboard.models import Message, Quote
from dashboard.forms import ProjectForm
from accounts.forms import AddressInfoForm
from dashboard.decorators import allowed_users
from django.contrib.auth.decorators import login_required
import ast


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def quotes(request):
    if request.user.groups.first().name == 'host':
        quotes = Quote.objects.all()
        return render(request, 'dashboard/host/quotes.html', {'quotes': quotes})
    else:
        if request.method == 'POST':

            projectForm = ProjectForm(request.POST)
            addressForm = AddressInfoForm(request.POST)

            body = {
                'bedrooms': request.POST['bedrooms'],
                'system_required': request.POST['system_required'],
                'system_control': request.POST['system_control'],
                'description': request.POST['description']
            }

            # form = QuotesForm()

            summary = body['description'] if len(
                body['description']) < 50 else body['description'][:33] + '...'

            # if form.is_valid:
            # instance = form.save(commit=False)
            # instance.user = request.user
            # instance.save()
            quote = Quote.objects.create(
                description=body, user=request.user.userdetail)
            message = Message(
                creator=request.user.userdetail, body=body, summary=summary, quote=quote)

            message.save()

            # Save Address
            if addressForm.is_valid() and projectForm.is_valid():
                address = addressForm.save()
            # Save Project
                project = projectForm.save(commit=False)
                project.owner = request.user.userdetail
                project.quote = quote
                project.address = address

                project.save()

                return redirect('message')
            else:
                raise ValueError('Not valid')
        else:
            propertyForm = ProjectForm()
            addressForm = AddressInfoForm()

            # if request.user.userdetail.quote:
            #     quote = ast.literal_eval(
            #         request.user.userdetail.project.quote.description)

            return render(request, 'dashboard/user/quotes.html', {'propertyForm': propertyForm, 'addressForm': addressForm})
