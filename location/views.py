from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Teacher
from .models import *
from .forms import *


@login_required
def LocationView(request):
    if request.POST:
        user = request.user
        teacher = Teacher.objects.filter(user=user)[0]

        name = request.POST['name']
        description = request.POST['description']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
 

        if name == '' or description == '' or latitude == '' or longitude == '':
            messages.error(request,"Campos inválidos")
        else:
            try:
                Location.objects.create(name=name,teacher=teacher,description=description,latitude=float(latitude),longitude=float(longitude))
                messages.success(request,"Localização criada com sucesso")
            except:
                messages.error(request,"Campos inválidos")

        return render(request, 'location/Location.html')
    else:
        return render(request, 'location/Location.html')


