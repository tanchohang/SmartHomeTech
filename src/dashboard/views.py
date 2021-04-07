from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'dashboard/user/overview.html')


def quotes(request):
    return render(request, 'dashboard/user/quotes.html')


def profile(request):
    return render(request, 'dashboard/user/profile.html')


def messages(request):
    return render(request, 'dashboard/user/messages.html')


def message_detail(request):
    return render(request, 'dashboard/user/message-detail.html')

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
