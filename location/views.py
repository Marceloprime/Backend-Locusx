from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def LocationView(request):
    getUser = request.user
    getteacher = Teacher.objects.filter(user=getUser).values_list('id', flat = True)[0]
    locations = Location.objects.filter(teacher=getteacher)
    print(locations)
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
        'form': form,
        'locations': locations
    }
    return render(request, 'location/Location.html',context)
