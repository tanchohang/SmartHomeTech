from django.shortcuts import render, redirect
from ..models import Message, Reply, Appointment
from django.contrib.auth.models import User
from ..forms import MessageForm, AppointmentForm


def messages(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('/dashboard/messages')
    else:
        form = MessageForm()
        messages = Message.objects.filter(creator=request.user.id)
        return render(request, 'dashboard/user/messages.html', {'messages': messages, 'form': form})


def message_detail(request, id):

    if request.method == 'POST':
        print(request.POST)
        reply = Reply()
        reply.body = request.POST.get('body')
        reply.message = Message.objects.get(id=id)
        reply.author = request.user
        reply.save()

        replies = Reply.objects.filter(message=id)
        return redirect('/dashboard/messages/'+id)
    else:
        appointmentForm = AppointmentForm()
        message = Message.objects.get(id=id)
        replies = Reply.objects.filter(message=id)

        return render(request, 'dashboard/user/message-detail.html', {'message': message, 'replies': replies, 'user': request.user})


def message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/dashboard/messages')


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

        return redirect('/dashboard/appointment')

    else:
        form = AppointmentForm()
        return render(request, 'dashboard/user/appointment.html', {'form': form})
