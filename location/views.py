from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Teacher
from .models import *
from .forms import *


@login_required
def LocationView(request):
    user = request.user
    teacher = Teacher.objects.filter(user=user)[0]
    locations = Location.objects.filter(teacher=teacher).order_by('-modified_at')
    context = {
        'locations' : locations,
    }
    if request.POST:
        user = request.user
        teacher = Teacher.objects.filter(user=user)[0]

        name = request.POST['name']
        description = request.POST['description']
        coordinates = request.POST['coordinates'].split(', ')

        try:
            Location.objects.create(name=name,teacher=teacher,description=description,latitude=float(coordinates[0]),longitude=float(coordinates[1]))
            messages.success(request,"Localização criada com sucesso")
        except:
            messages.error(request,"Campos inválidos")

        return render(request, 'location/Location.html',context)
    else:
        return render(request, 'location/Location.html',context)


