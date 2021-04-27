from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def LocationView(request):
    if str(request.method) == 'POST':
        form = LocationModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Localização salvo com sucesso')
            form = LocationModelForm()
        else:
            messages.error(request, 'Erro ao salvar localização')
    else:
        form = LocationModelForm()

    context = {
        'form': form
    }
    return render(request, 'location/Location.html',context)
