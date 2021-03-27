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

#################################################################