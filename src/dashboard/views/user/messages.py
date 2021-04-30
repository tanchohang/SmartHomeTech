from django.shortcuts import render, redirect
from dashboard.models import Message, Appointment, Project, Quote

from dashboard.forms import MessageForm, AppointmentForm, FileForm
from dashboard.models import ProjectFiles, Project
from accounts.models import UserDetail
from dashboard.decorators import allowed_users
from django.contrib.auth.decorators import login_required

import datetime
import ast


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def messages(request):

    if request.user.groups.first().name == 'host':

        if request.method == 'POST':
            form = MessageForm(request.POST, request.FILES)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user.userdetail
                instance.save()
                return redirect('message')
        else:
            form = MessageForm()
            messages = Message.objects.all()
            return render(request, 'dashboard/user/messages.html', {'messages': messages, 'form': form})
    else:

        if request.method == 'POST':
            form = MessageForm(request.POST)
            fileform = FileForm(request.POST, request.FILES)
            files = request.FILES.getlist('files')
            if form.is_valid() and fileform.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user.userdetail
                instance.save()
                for file in files:
                    file_instance = ProjectFiles(files=file, message=instance)
                    file_instance.save()
                return redirect('message')
        else:
            form = MessageForm()
            fileform = FileForm()

            messages = Message.objects.filter(
                creator=request.user.userdetail)
            projects = Project.objects.filter(
                owner_id=request.user.userdetail.id)
            return render(request, 'dashboard/user/messages.html', {'messages': messages, 'form': form, 'fileform': FileForm, 'projects': projects})


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def message_detail(request, id):

    # View For host
    if request.user.groups.first().name == 'host':

        if request.method == 'POST':
            messageForm = MessageForm(request.POST)
            fileform = FileForm(request.POST, request.FILES)

            if messageForm.is_valid():

                message = Message.objects.get(id=id)

                instance = messageForm.save(commit=False)
                instance.creator = request.user.userdetail
                instance.project = message.project
                instance.save()

                return redirect('message-detail', id)
            else:
                raise ValueError('Forms not Valid')
        else:

            appointmentForm = AppointmentForm()
            message = Message.objects.get(id=id)
            messages = Message.objects.filter(
                project_id=message.project).exclude(subject='quote')
            quote = {}
            if message.project:
                quote = ast.literal_eval(message.body)

            messageForm = MessageForm()
            fileform = FileForm()
            return render(request, 'dashboard/user/message-detail.html', {'message': message, 'messages': messages, 'messageForm': messageForm, 'fileform': fileform, 'quote': quote})

    # View For Users
    else:

        if request.method == 'POST':
            messageForm = MessageForm(request.POST)
            fileform = FileForm(request.POST, request.FILES)

            if messageForm.is_valid():

                message = Message.objects.get(id=id)

                instance = messageForm.save(commit=False)
                instance.creator = request.user.userdetail
                instance.project = message.project
                instance.save()

                return redirect('message-detail', id)
            else:
                raise ValueError('Forms not Valid')
        else:
            appointmentForm = AppointmentForm()
            message = Message.objects.get(id=id)

            messages = Message.objects.filter(
                project_id=message.project).exclude(subject='quote')
            quote = {}
            if message.project:
                quote = ast.literal_eval(message.body)

            messageForm = MessageForm()
            fileform = FileForm()
            return render(request, 'dashboard/user/message-detail.html', {'message': message, 'messages': messages, 'messageForm': messageForm, 'fileform': fileform, 'quote': quote, 'appointmentForm': appointmentForm})


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/user/messages')


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def appointment(request, appointment):
    if request.method == 'POST':
        appointment_instance = Appointment.objects.get(id=appointment)
        form = AppointmentForm(
            instance=appointment_instance, data=request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.is_confirmed = True
            appointment.save()
            return redirect('projects')
        else:
            raise ValueError('form invalid')
