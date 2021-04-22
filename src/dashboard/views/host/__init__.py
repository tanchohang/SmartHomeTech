from django.shortcuts import render, redirect

from dashboard.models import Message, Reply, Quote
from accounts.models import UserDetail
from django.contrib.auth.models import User

from dashboard.forms import MessageForm

from dashboard.decorators import allowed_users
from django.contrib.auth.decorators import login_required

# Host Views


# @login_required(login_url='login')
# @allowed_users(allowed_groups=['host'])
# def dashboard(request):
#     return render(request, 'dashboard/host/overview.html')


@login_required(login_url='login')
@allowed_users(allowed_groups=['host'])
def users(request):
    endusers = User.objects.filter(groups__name='end-user')
    contractors = User.objects.filter(groups__name='contractor')
    return render(request, 'dashboard/host/users.html', {'endusers': endusers, 'contractors': contractors})


@login_required(login_url='login')
@allowed_users(allowed_groups=['host'])
def quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'dashboard/host/quotes.html', {'quotes': quotes})


@login_required(login_url='login')
@allowed_users(allowed_groups=['host'])
def messages(request):

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


@login_required(login_url='login')
@allowed_users(allowed_groups=['host'])
def message_delete(request, id):
    message = Message.objects.filter(id=id).delete()
    return redirect('/dashboard/messages')


@login_required(login_url='login')
@allowed_users(allowed_groups=['host'])
def assign_contractor(request, user_id, contractor_id):
    user = UserDetail.objects.get(user_id=user_id)
    contractor = UserDetail.objects.get(user_id=contractor_id)
    user.contractor = (contractor)
    user.save()

    # user.save()
    return redirect('users')
