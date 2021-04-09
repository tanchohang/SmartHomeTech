from django.shortcuts import render

from .quotes import *
from .messages import *


# Create your views here.


def home(request):
    return render(request, 'dashboard/user/overview.html')


def profile(request):
    return render(request, 'dashboard/user/profile.html')


# Contractor views


def contractor_home(request):
    return render(request, 'dashboard/contractor/overview.html')


def contractor_quotes(request):
    return render(request, 'dashboard/contractor/quotes.html')


def contractor_profile(request):
    return render(request, 'dashboard/contractor/profile.html')


def contractor_messages(request):
    return render(request, 'dashboard/contractor/messages.html')


def contractor_message_detail(request):
    return render(request, 'dashboard/contractor/message-detail.html')


# Host Views

def host_home(request):
    return render(request, 'dashboard/host/overview.html')


def host_quotes(request):
    return render(request, 'dashboard/host/quotes.html')


def host_profile(request):
    return render(request, 'dashboard/host/profile.html')


def host_messages(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('/dashboard/messages')
    else:
        form = MessageForm()
        messages = Message.objects.all()
        return render(request, 'dashboard/user/messages.html', {'messages': messages, 'form': form})


def host_message_detail(request, id):

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

        message = Message.objects.get(id=id)
        replies = Reply.objects.filter(message=id)

        return render(request, 'dashboard/user/message-detail.html', {'message': message, 'replies': replies, 'user': request.user})


def host_message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/dashboard/messages')
