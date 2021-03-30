from accounts.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json
from accounts.api.serializers import *
from .permissions import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
  """
    queryset = User.objects.none()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'],detail=False)
    def myprofile(self, request):
      
      if str(request.user) != "AnonymousUser":
        list_json = serializers.serialize("json", User.objects.all())
        data = {
          "username":str(request.user.username),
          "email":str(request.user.email),
          "is_student":str(request.user.is_student),
          "is_teacher":str(request.user.is_teacher),
          "is_institution_adm":str(request.user.is_institution_adm),
        }
        return Response(data)
      else:
        print(request.user )
        return Response({"Messagem":"Usuário não atorizado, tente realizar o login ou crie uma conta"})
      
############################################################################################
# Users

class Institution_admViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyAdmin]
  serializer_class = Institution_admSerializers
  queryset = Institution_adm.objects.all()

  
class TeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = TeacherSerializers
  queryset = Teacher.objects.all()


############################################################################################
###         instituicao
class CourseViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyAdmin]
  serializer_class = CourseSerializers
  def get_queryset(self):
      getUser = self.request.user
      getAdm = Institution_adm.objects.filter(user=getUser)
      getID = getAdm.values_list('id', flat = True)
      getInfo = getID[0]
      return  Course.objects.filter(adm=getInfo)

  @action(methods=['get'],detail=True)
  def get_class(self, request,pk):
      the_class = Class.objects.filter(pk=pk)
      id = the_class.values_list('id', flat = True)[0]
      name = the_class.values_list('name', flat = True)[0]
      description = the_class.values_list('description', flat = True)[0]
      created_at = str(the_class.values_list('created_at', flat = True)[0])
      modified_at = str(the_class.values_list('modified_at', flat = True)[0])
      adm = the_class.values_list('adm', flat = True)[0]
      program = the_class.values_list('program', flat = True)[0]

      objadm = Institution_adm.objects.filter(id=adm)
      id_adm = objadm.values_list('user', flat = True)[0]
      objadm = User.objects.filter(id=id_adm)
      #print(objadm)

      adm = {
        "username" : objadm.values_list('username', flat = True)[0],
        "email" : objadm.values_list('email', flat = True)[0],
        "first_name" : objadm.values_list('first_name', flat = True)[0],
        "lastname" : objadm.values_list('first_name', flat = True)[0],
        "id_adm" : Institution_adm.objects.filter(id=adm).values_list('user', flat = True)[0],
        "id_user" : objadm.values_list('id', flat = True)[0],
      }

      objprogram = Program.objects.filter(id=program)
   
      program = {
        "name" : objprogram.values_list('name', flat = True)[0],
        "description" : objprogram.values_list('description', flat = True)[0],
      }

      data = {
        "id" : id,
        "name" : name,
        "description" : description,
        "created_at" : created_at,
        "modified_at" : modified_at,
        "adm" : adm,
        "program" : program
      }

      return Response(data)


class ProgramViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyAdmin]
  serializer_class = ProgramSerializers
  def get_queryset(self):
      getUser = self.request.user
      getAdm = Institution_adm.objects.filter(user=getUser)
      getID = getAdm.values_list('id', flat = True)
      getInfo = getID[0]
      return  Program.objects.filter(adm=getInfo)

class ClassViewset(viewsets.ModelViewSet):
  permission_classes = [OnlyUsers]
  serializer_class = ClassSerializers
  queryset = Class.objects.all()

  @action(methods=['get'],detail=False)
  def get_student_class(self, request):
    getUser = self.request.user
    get_student = Student.objects.filter(user=getUser)
    getID = get_student.values_list('id', flat = True)
    classes = Class.objects.filter(students=getID[0])
    data = []

    
    for classe in classes:
    
      DataJson = {
        "id" : classe.id,
        "name" : str(classe),
        "description" : str(classe.description),
        "program" : str(classe.program),
      }
     
      data.append(DataJson)
   
    return Response(data)

  @action(methods=['get'],detail=False)
  def get_teacher_class(self, request):
    getUser = self.request.user
    get_student = Teacher.objects.filter(user=getUser)
    getID = get_student.values_list('id', flat = True)
    classes = Class.objects.filter(teachers=getID[0])
    data = []
    print(classes)
    for classe in classes:
      DataJson = {
        "id" : classe.id,
        "name" : str(classe),
        "description" : str(classe.description),
        "program" : str(classe.program),
      }
     
      data.append(DataJson)

    return Response(data)

#################################################################
###         Teacher
class CourseTeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyTeachers]
  serializer_class = CourseTeacherSerializers

  def get_queryset(self):
      getUser = self.request.user
      getTeacher = Teacher.objects.filter(user=getUser)
      getID = getTeacher.values_list('id', flat = True)
      getInfo = getID[0]
      return  CourseTeacher.objects.filter(teacher=getInfo)
  
  @action(methods=['get'],detail=True)
  def get_class(self, request,pk):
      the_class = ClassTeacher.objects.filter(pk=pk)
      id = the_class.values_list('id', flat = True)[0]
      name = the_class.values_list('name', flat = True)[0]
      description = the_class.values_list('description', flat = True)[0]
      created_at = str(the_class.values_list('created_at', flat = True)[0])
      modified_at = str(the_class.values_list('modified_at', flat = True)[0])
      teacher = the_class.values_list('teacher', flat = True)[0]
      program = the_class.values_list('program', flat = True)[0]

      objTeacher = Teacher.objects.filter(id=teacher)
      id_teacher = objTeacher.values_list('user', flat = True)[0]
      objTeacher = User.objects.filter(id=id_teacher)

      teacher = {
        "username" : objTeacher.values_list('username', flat = True)[0],
        "email" : objTeacher.values_list('email', flat = True)[0],
        "first_name" : objTeacher.values_list('first_name', flat = True)[0],
        "lastname" : objTeacher.values_list('first_name', flat = True)[0],
        "id_teacher" : Teacher.objects.filter(id=teacher).values_list('user', flat = True)[0],
        "id_user" : objTeacher.values_list('id', flat = True)[0],
      }

      objprogram = ProgramTeacher.objects.filter(id=program)
   
      program = {
        "name" : objprogram.values_list('name', flat = True)[0],
        "description" : objprogram.values_list('description', flat = True)[0],
      }

      data = {
        "id" : id,
        "name" : name,
        "description" : description,
        "created_at" : created_at,
        "modified_at" : modified_at,
        "teacher" : teacher,
        "program" : program
      }

      return Response(data)


class ProgramTeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyTeachers]
  serializer_class = ProgramTeacherSerializers
  def get_queryset(self):
      getUser = self.request.user
      getTeacher = Teacher.objects.filter(user=getUser)
      getID = getTeacher.values_list('id', flat = True)
      getInfo = getID[0]
      return  ProgramTeacher.objects.filter(teacher=getInfo)

class ClassTeacherViewset(viewsets.ModelViewSet):
  permission_classes = [OnlyUsers]
  serializer_class = ClassTeacherSerializers
  queryset = ClassTeacher.objects.all()

  @action(methods=['get'],detail=False)
  def get_student_class(self, request):
    getUser = self.request.user
    get_student = Student.objects.filter(user=getUser)
    getID = get_student.values_list('id', flat = True)
    classes = ClassTeacher.objects.filter(students=getID[0])
    data = []

    
    for classe in classes:
    
      DataJson = {
        "id" : classe.id,
        "name" : str(classe),
        "description" : str(classe.description),
        "program" : str(classe.program),
      }
     
      data.append(DataJson)
   
    return Response(data)

  @action(methods=['get'],detail=False)
  def get_teacher_class(self, request):
    getUser = self.request.user
    get_student = Teacher.objects.filter(user=getUser)
    getID = get_student.values_list('id', flat = True)
    classes = ClassTeacher.objects.filter(teacher=getID[0])
    data = []

    for classe in classes:
      DataJson = {
        "id" : classe.id,
        "name" : str(classe),
        "description" : str(classe.description),
        "program" : str(classe.program),
      }
     
      data.append(DataJson)

    return Response(data)

#################################################################
class InstitutionViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyAdmin]
  serializer_class = InstitutionSerializers
  queryset = Institution.objects.all()

  @action(methods=['get'],detail=False)
  def allusers(self, request):
    getUser = self.request.user
    getAdm = Institution_adm.objects.filter(user=getUser)[0]
    getInstituition = Institution.objects.filter(user=getAdm)
    name = getInstituition.values_list('name', flat = True)[0]
    teachers = getInstituition.values_list('teachers', flat = True)
    students = getInstituition.values_list('student', flat = True)

    teachers_json = []
    students_json = []

    for teacher in teachers:
      objTeacher = Teacher.objects.filter(id=teacher)
      id_teacher = objTeacher.values_list('user', flat = True)[0]
      objTeacher = User.objects.filter(id=id_teacher)

      data = {
        "username" : objTeacher.values_list('username', flat = True)[0],
        "email" : objTeacher.values_list('email', flat = True)[0],
        "first_name" : objTeacher.values_list('first_name', flat = True)[0],
        "lastname" : objTeacher.values_list('first_name', flat = True)[0],
        "id_teacher" : Teacher.objects.filter(id=teacher).values_list('user', flat = True)[0],
        "id_user" : objTeacher.values_list('id', flat = True)[0],
      }

      teachers_json.append(data)

    for student in students:
      objStudent = Student.objects.filter(id=student)
      id_student = objStudent.values_list('user', flat = True)[0]
      objStudent = User.objects.filter(id=id_student)

      data = {
        "username" : objStudent.values_list('username', flat = True)[0],
        "email" : objStudent.values_list('email', flat = True)[0],
        "first_name" : objStudent.values_list('first_name', flat = True)[0],
        "lastname" : objStudent.values_list('first_name', flat = True)[0],
        "id_teacher" : Student.objects.filter(id=student).values_list('user', flat = True)[0],
        "id_user" : objStudent.values_list('id', flat = True)[0],
      }

      students_json.append(data)

    intitution_json = {
      "name" : name,
      "teachers" : teachers_json,
      "students" : students_json
    }
    return Response(intitution_json)
  
  @action(detail=False, methods=['put'])
  def addteacher(self, request):
    email = request.data.get('email')
    id_teacher = User.objects.filter(email=email).values_list('id', flat = True)[0]

    teacher = Teacher.objects.get(user=id_teacher)

    teacherName = User.objects.filter(email=email).values_list('email', flat = True)[0]

    getUser = request.user
    getAdm = Institution_adm.objects.filter(user=getUser)[0]
    getInstituition = Institution.objects.get(user=getAdm)
    InstituitionName = Institution.objects.filter(user=getAdm).values_list('name', flat = True)[0]
    getInstituition.teachers.add(teacher)

    return Response({"Mesangem": "O " +  teacherName + " foi adicionado a " + InstituitionName})

class AddressViewSet(viewsets.ModelViewSet):
  permission_classes = [OnlyAdmin]
  serializer_class = AddressSerializers
  queryset = Address.objects.all()

