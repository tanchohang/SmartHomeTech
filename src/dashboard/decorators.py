from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_groups:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, '../../404.html')

        return wrapper_func
    return decorator
