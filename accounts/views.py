from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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
            'user' : User.objects.filter(email=request.user)
        }
    except:
        context = {
            'user' : "não deu bom"
        }

    return render(request, 'home.html',context)


def singup(request):
    print(request.POST)
    try:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        type_user = request.POST['type_user']

        return render(request, 'singup.html')
    except:
        print("erro")
        return render(request, 'singup.html')

def Institution(request):
    if str(request.method) == 'POST':
        form = InstitutionModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instituição salvo com sucesso')
            form = InstitutionModelForm()
        else:
            messages.error(request, 'Erro ao salvar Instituição')
    else:
        form = InstitutionModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/Institution.html',context)
