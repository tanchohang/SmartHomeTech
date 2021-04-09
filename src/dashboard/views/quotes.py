from django.shortcuts import render, redirect
from ..forms import QuotesForm
from ..models import Message


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

        message = Message(
            user=request.user, body=body, summary=summary)

        message.save()
        return redirect('/dashboard/messages')
    else:

        return render(request, 'dashboard/user/quotes.html')
