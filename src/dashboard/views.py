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