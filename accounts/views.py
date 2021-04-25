from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
def index(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user.is_authenticated == True:
            login(request, user)
            # Redirect to a success page.
            return home(request,user)
        else:
            # Return an 'invalid login' error message.
            ...
            return render(request, 'erro.html')

    except:
        return render(request, 'index.html')

    return render(request, 'index.html')

@login_required
def home(request,user):

    userData = User.objects.filter(email=user)
    context = {
        'user' : userData
    }
    return render(request, 'home.html',context)


def erro(request):
    return render(request, 'erro.html')