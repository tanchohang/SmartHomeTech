from django.shortcuts import render, redirect
from dashboard.models import Message, Reply, Appointment
# from django.contrib.auth.models import User
from dashboard.forms import MessageForm, AppointmentForm, FileForm
from dashboard.models import MessageFiles

import ast


def messages(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        fileform = FileForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid() and fileform.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            for file in files:
                file_instance = MessageFiles(files=file, message=instance)
                file_instance.save()
            return redirect('/user/messages')
    else:
        form = MessageForm()
        fileform = MessageForm()
        messages = Message.objects.filter(creator=request.user.id)

        return render(request, 'dashboard/user/messages.html', {'messages': messages, 'form': form, 'fileform': FileForm})


def message_detail(request, id):

    if request.method == 'POST':
        print(request.POST)
        reply = Reply()
        reply.body = request.POST.get('body')
        reply.message = Message.objects.get(id=id)
        reply.author = request.user
        reply.save()

        replies = Reply.objects.filter(message=id)
        return redirect('/user/messages/'+id)
    else:
        appointmentForm = AppointmentForm()
        message = Message.objects.get(id=id)
        quote = {}
        if message.quote:
            quote = ast.literal_eval(message.body)

        replies = Reply.objects.filter(message=id)

        return render(request, 'dashboard/user/message-detail.html', {'message': message, 'replies': replies, 'user': request.user, 'quote': quote})


def message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/user/messages')


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():

            appointment = Appointment()
            appointment.date = form.cleaned_data['date'],
            appointment.time = form.cleaned_data['time'],
            appointment.preference = form.cleaned_data['preference'],
            appointment.phone = form.cleaned_data['phone']
            appointment.user = request.user
            # appointment.save()
            print(type(form.cleaned_data['date']))

        return redirect('/user/appointment')

    else:
        form = AppointmentForm()
        return render(request, 'dashboard/user/appointment.html', {'form': form})
