from django.shortcuts import render, redirect

from dashboard.models import Message, Reply, Quote
from accounts.models import EndUser, Contractor
from dashboard.forms import MessageForm


# Host Views

def dashboard(request):
    return render(request, 'dashboard/host/overview.html')


def users(request):
    endusers = EndUser.objects.all()
    contractors = Contractor.objects.all()
    return render(request, 'dashboard/host/users.html', {'endusers': endusers, 'contractors': contractors})


def quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'dashboard/host/quotes.html', {'quotes': quotes})


def profile(request):
    return render(request, 'dashboard/host/profile.html')


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
        messages = Message.objects.all()
        return render(request, 'dashboard/host/messages.html', {'messages': messages, 'form': form})


def message_detail(request, id):

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


def message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/dashboard/messages')
