from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
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
def logout_view(request):
    print("oi")
    logout(request)
    # Redirect to a success page
    return redirect('home/')

@login_required
def home(request):
    try:
        if request.user.is_institution_adm == True:
          getUser = request.user
          getAdm = Institution_adm.objects.filter(user=getUser).values_list('id', flat = True)[0]
          
          data = {
            "username":str(request.user.username),
            "email":str(request.user.email),
            "first_name":str(request.user.first_name),
            "last_name":str(request.user.last_name),
            "is_student": request.user.is_student,
            "is_teacher": request.user.is_teacher,
            "is_institution_adm": request.user.is_institution_adm,
            "adm_id": getAdm
          }

        elif request.user.is_teacher == True:
          getUser = request.user
          getTeacher = Teacher.objects.filter(user=getUser).values_list('id', flat = True)[0]

          try:
            institutions = Institution.objects.filter(teachers=getTeacher)
          except:
            institutions = False

          try:
            institutionsTeacher = Institution.objects.filter(teachers=getTeacher)
            dataInstitution = []

            for insti in institutionsTeacher:
      
              aux = {
                "name" : insti.name,
                "description" : insti.description
              }
              dataInstitution.append(aux)
            dataInstitution =  json.dumps(dataInstitution,ensure_ascii=False).encode('utf8')
          except:
            dataInstitution = []

          data = {
            "username":str(request.user.username),
            "email":str(request.user.email),
            "first_name":str(request.user.first_name),
            "last_name":str(request.user.last_name),
            "is_student": request.user.is_student,
            "is_teacher": request.user.is_teacher,
            "is_institution_adm": request.user.is_institution_adm,
            "user_id": request.user.id,
            "teacher_id" : getTeacher,
            "institutions": dataInstitution
          }

        elif request.user.is_student == True:
          getUser = request.user
          getStudent = Student.objects.filter(user=getUser).values_list('id', flat = True)[0]
          data = {
            "username":str(request.user.username),
            "email":str(request.user.email),
            "first_name":str(request.user.first_name),
            "last_name":str(request.user.last_name),
            "is_student": request.user.is_student,
            "is_teacher": request.user.is_teacher,
            "is_institution_adm": request.user.is_institution_adm,
            "student_id": getStudent
          }
        else:
          data = {
            "username":str(request.user.username),
            "email":str(request.user.email),
            "first_name":str(request.user.first_name),
            "last_name":str(request.user.last_name),
            "is_student": request.user.is_student,
            "is_teacher": request.user.is_teacher,
            "is_institution_adm": request.user.is_institution_adm,
        }

        context = {
            'user' : data
        }
    except:
        context = {
            'user' : "NOT FOUND"
        }

    print(context)
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

def InstitutionView(request):
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

def AddressView(request):
    if str(request.method) == 'POST':
        form = AddressModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Endereço salvo com sucesso')
            form = AddressModelForm()
        else:
            messages.error(request, 'Erro ao salvar Endereço')
    else:
        form = AddressModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/Address.html',context)

###########################################################################
#                       Instituicao                                       #

def ProgramView(request):
    if str(request.method) == 'POST':
        form = ProgramModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Programa salvo com sucesso')
            form = ProgramModelForm()
        else:
            messages.error(request, 'Erro ao salvar Programa')
    else:
        form = ProgramModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/Program.html',context)

def ClassView(request):
    if str(request.method) == 'POST':
        form = ClassModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classe salvo com sucesso')
            form = ClassModelForm()
        else:
            messages.error(request, 'Erro ao salvar Classe')
    else:
        form = ClassModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/Class.html',context)

def CourseView(request):
    if str(request.method) == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso salvo com sucesso')
            form = CourseModelForm()
        else:
            messages.error(request, 'Erro ao salvar Curso')
    else:
        form = CourseModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/Course.html',context)

###########################################################################
#                       Teacher                                           #
def ProgramTeacherView(request):
    if str(request.method) == 'POST':
        form = ProgramTeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Programa salvo com sucesso')
            form = ProgramTeacherModelForm()
        else:
            messages.error(request, 'Erro ao salvar Programa')
    else:
        form = ProgramTeacherModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/ProgramTeacher.html',context)

def ClassTeacherView(request):
    if str(request.method) == 'POST':
        form = ClassTeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classe salvo com sucesso')
            form = ClassTeacherModelForm()
        else:
            messages.error(request, 'Erro ao salvar Classe')
    else:
        form = ClassTeacherModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/ClassTeacher.html',context)

def CourseTeacherView(request):
    if str(request.method) == 'POST':
        form = CourseTeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso salvo com sucesso')
            form = CourseTeacherModelForm()
        else:
            messages.error(request, 'Erro ao salvar Curso')
    else:
        form = CourseTeacherModelForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/CourseTeacher.html',context)