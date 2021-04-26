from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
def index(request):
    if(str(request.user) != "AnonymousUser"):
        return redirect('home/')
    
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home/')
        else:
            # Return an 'invalid login' error message.
            ...
            return render(request, 'index.html')

    except:
        return render(request, 'index.html')

    return render(request, 'index.html')

@login_required
def home(request):
    try:

        context = {
            'user' : request.user
        }
    except:
        context = {
            'user' : "não deu bom"
        }

    print(request.user)
    return render(request, 'home.html',context)


def erro(request):
    return render(request, 'erro.html')