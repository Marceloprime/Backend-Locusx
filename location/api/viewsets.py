from location.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json
from location.api.serializers import *
from .permissions import *

class LocationViewSet(viewsets.ModelViewSet):
  #permission_classes = [OnlyTeachersOrStudents]
  serializer_class = LocationSerializers
  
  def get_queryset(self):
    if str(self.request.user) != "AnonymousUser":
      getUser = self.request.user
      getteacher = Teacher.objects.filter(user=getUser).values_list('id', flat = True)[0]
      return  Location.objects.filter(teacher=getteacher)
    else:
      return Location.objects.none()

  def create(self, request):
    getUser = self.request.user
    getteacher = Teacher.objects.filter(user=getUser).values_list('id', flat = True)[0]
    ObjLocation = Location()
    ObjLocation.name = request.data.get('name')
    ObjLocation.teacher_id = getteacher
    ObjLocation.latitude = request.data.get('latitude')
    ObjLocation.longitude = request.data.get('longitude')
    ObjLocation.save()
    
    responseJson = {
      "name" : request.data.get('name'),
      "latitude" : request.data.get('latitude'),
      "longitude" : request.data.get('longitude')
    }
    return Response(responseJson)