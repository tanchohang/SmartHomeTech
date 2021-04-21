from django.shortcuts import render, redirect
from dashboard.models import Message, Reply, Appointment
# from django.contrib.auth.models import User
from dashboard.forms import MessageForm, AppointmentForm, FileForm
from dashboard.models import MessageFiles
from dashboard.decorators import allowed_users
from django.contrib.auth.decorators import login_required


import ast


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def messages(request):

    if request.user.groups.first().name == 'host':

        if request.method == 'POST':
            form = MessageForm(request.POST, request.FILES)

            if form.is_valid:
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                return redirect('/dashboard/messages')
        else:
            form = MessageForm()
            messages = Message.objects.all()
            return render(request, 'dashboard/host/messages.html', {'messages': messages, 'form': form})
    else:

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


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def message_detail(request, id):

    if request.user.groups.first().name == 'host':

        if request.method == 'POST':
            print(request.POST)
            reply = Reply()
            reply.body = request.POST.get('body')
            reply.message = Message.objects.get(id=id)
            reply.author = request.user
            reply.save()

            replies = Reply.objects.filter(message=id)
            return redirect('/host/messages/'+id)
        else:

            message = Message.objects.get(id=id)
            replies = Reply.objects.filter(message=id)

            return render(request, 'dashboard/host/message-detail.html', {'message': message, 'replies': replies, 'user': request.user})

    else:

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


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/user/messages')


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
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

        return redirect('/user/appointment')

    else:
        form = AppointmentForm()
        return render(request, 'dashboard/user/appointment.html', {'form': form})
