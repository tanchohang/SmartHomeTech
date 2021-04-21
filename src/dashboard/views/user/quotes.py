from django.shortcuts import render, redirect
from dashboard.forms import QuotesForm
from dashboard.models import Message, Quote
from dashboard.decorators import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@allowed_users(allowed_groups=['end-user', 'contractor', 'host'])
def quotes(request):
    if request.user.groups.first().name == 'host':
        quotes = Quote.objects.all()
        return render(request, 'dashboard/host/quotes.html', {'quotes': quotes})
    else:
        if request.method == 'POST':

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
            quote = Quote.objects.create(description=body, user=request.user)
            message = Message(
                creator=request.user, body=body, summary=summary, quote=quote)

            message.save()
            return redirect('/user/messages')
        else:

            return render(request, 'dashboard/user/quotes.html')
