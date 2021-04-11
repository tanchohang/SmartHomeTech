from django.shortcuts import render, redirect
from dashboard.forms import QuotesForm
from dashboard.models import Message, Quote


def quotes(request):

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
