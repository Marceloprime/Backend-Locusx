from rest_framework import serializers
from location.models import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'