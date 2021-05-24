from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext as _
from django.utils import translation
from django.http  import HttpResponse
import json

# My models
from location.models import Location
from content.models import *
from .models import *
from .forms import *

def index(request):
    if(str(request.user) != "AnonymousUser"):
        return redirect('home')
    
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            ...
            return render(request, 'index.html')

    except:
        return render(request, 'index.html')

    return render(request, 'index.html')

@login_required
def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('index')

@login_required
def home(request):
    if request.POST:
        type_user = request.POST['type_user']
        if type_user == 'is_student':
            is_student = True
            is_teacher = False
            is_institution_adm = False
        elif type_user == 'is_teacher':
            is_student = False
            is_teacher = True
            is_institution_adm = False
        elif type_user == 'is_institution_adm':
            is_student = False
            is_teacher = False
            is_institution_adm = True

        if is_student == True: 
            user = User.objects.filter(email=request.user).update(is_student=True)
            Token.objects.create(user=request.user)
            Student.objects.create(user=request.user)
        elif is_teacher == True:
            user = User.objects.filter(email=request.user).update(is_teacher=True)
            Token.objects.create(user=request.user)
            Teacher.objects.create(user=request.user) 
        elif is_institution_adm == True:
            user = User.objects.filter(email=request.user).update(is_institution_adm=True)
            Token.objects.create(user=request.user)
            Institution_adm.objects.create(user=request.user) 

        return redirect('index')
    
    locations = []
    program = []
    programTeacher = []
    classes = []
    classesTeacher = []
    course = []
    courseTeacher = []
    atividades = []

    lang = translation.get_language()
    translation.activate(lang)

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

          locations = Location.objects.filter(teacher=getTeacher).order_by('-modified_at')

          classes = Class.objects.filter(teachers=getTeacher)
          classesTeacher = ClassTeacher.objects.filter(teacher=getTeacher)

          program = Program.objects.filter(teachers=getTeacher)
          programTeacher = ProgramTeacher.objects.filter(teacher=getTeacher)

          course = Course.objects.filter(teachers=getTeacher)
          courseTeacher = CourseTeacher.objects.filter(teacher=getTeacher)

          try:
            atividades = ActivityTeacher.objects.filter(teacher=getTeacher)
          except:
            atividades = []

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
            "institutions": dataInstitution,
            "locations": locations,
            "classes": classes,
            "classesTeacher": classesTeacher,
            "program":program,
            "programTeacher":programTeacher,
            "course":course,
            "courseTeacher": courseTeacher,
            "atividades": atividades
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
        print(data)
        context = {
            'user' : data,
            'lang': lang
        }
    except:
        context = {
            'user' : "NOT FOUND",
            'lang': lang
        }

    print(context)
    return render(request, 'home.html',context)


def singup(request):
    if request.POST:
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            type_user = request.POST['type_user']
            is_active = True
            username = email
            
            if type_user == 'is_student':
                is_student = True
                is_teacher = False
                is_institution_adm = False
            elif type_user == 'is_teacher':
                is_student = False
                is_teacher = True
                is_institution_adm = False
            elif type_user == 'is_institution_adm':
                is_student = False
                is_teacher = False
                is_institution_adm = True
            

            if is_student == True: 
                user = User.objects._create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_active=is_active,is_student=is_student,is_teacher=is_teacher,is_institution_adm=is_institution_adm)
                Token.objects.create(user=user)
                Student.objects.create(user=user)
            elif is_teacher == True:
                user = User.objects._create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_active=is_active,is_student=is_student,is_teacher=is_teacher,is_institution_adm=is_institution_adm)
                Token.objects.create(user=user)
                Teacher.objects.create(user=user) 
            elif is_institution_adm == True:
                user = User.objects._create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_active=is_active,is_student=is_student,is_teacher=is_teacher,is_institution_adm=is_institution_adm)
                Token.objects.create(user=user)
                Institution_adm.objects.create(user=user) 
            else:
                User.objects._create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_active=is_active,is_student=is_student,is_teacher=is_teacher,is_institution_adm=is_institution_adm)
                Token.objects.create(user=user) 

            try:
                user = authenticate(request, email=username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('home')
                else:
                    # Return an 'invalid login' error message.
                    messages.error(request, 'Campos inválidos')
                    return render(request, 'singup.html')
            except:
                return render(request, 'singup.html')
        except:
            messages.error(request, 'Campos inválidos')
    else:
        return render(request, 'singup.html')

@login_required
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

@login_required
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
@login_required
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

@login_required
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

@login_required
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
#                       Teacher   
# @login_required
@login_required                                        #
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

@login_required
def CreateclassTeacherView(request):
    return render(request, 'accounts/CreateClassTeacher.html')

@login_required
def ClassTeacherView(request):
    if request.POST:
        email = request.POST['email']
        class_id = request.POST['classe']
        try:
            user = User.objects.filter(email=email)[0]
            try:
                student = Student.objects.filter(user=user)[0]
                
                if student == None:
                    messages.error(request, 'Usuário não é estudante na base Locus X')
                else:
                    already_exists = ClassTeacher.objects.filter(id=class_id,students=student)[0]
                    if already_exists == None:
                        classe = ClassTeacher.objects.filter(id=class_id)[0]
                        classe.students.add(student)
                    else:
                        messages.error(request, 'Usuário já cadastrado')
            except:
                messages.error(request, 'Usuário não é estudante na base Locus X')
        except:
            messages.error(request, 'Usuário não cadastrado na base Locus X')

        #messages.error(request, 'Usuário não cadastrado na base Locus X')

    user = request.user
    getTeacher = Teacher.objects.filter(user=user).values_list('id', flat = True)[0]
    classesTeacher = ClassTeacher.objects.filter(teacher=getTeacher)
    students = []
    classrom = []
    for classe in classesTeacher:
        classrom = []
        studentsClass = ClassTeacher.objects.filter(id=classe.id).values_list('students',flat=True)
        for objects in studentsClass:
            aux = Student.objects.filter(id=objects).values_list('user',flat=True)[0]
            user = User.objects.filter(id=aux)[0]
            classrom.append(user)
        students.append(classrom)

    context = {
        'classes': classesTeacher,
        'students': students
    }
    return render(request, 'accounts/ClassTeacher.html',context)

@login_required
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