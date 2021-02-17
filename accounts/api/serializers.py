from rest_framework import serializers
from accounts.models import  User, Teacher, Student, Institution_adm, Institution, Address, Program, Class, Course, Teacher, Student, Institution_adm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    is_student = serializers.BooleanField(default=False)
    is_teacher = serializers.BooleanField(default=False)
    is_institution_adm = serializers.BooleanField(default=False)

    def create(self, validated_data):
        is_student = validated_data.get('is_student')
        is_teacher = validated_data.get('is_teacher')
        is_institution_adm = validated_data.get('is_institution_adm')
        content = {'res': 'criado com sucesso'}
        

        if is_student == True: 
            user = User.objects._create_user(**validated_data) 
            Token.objects.create(user=user)
            return Student.objects.create(user=user)
        elif is_teacher == True:
            user = User.objects._create_user(**validated_data) 
            Token.objects.create(user=user)
            return Teacher.objects.create(user=user) 
        elif is_institution_adm == True:
            user = User.objects._create_user(**validated_data) 
            Token.objects.create(user=user)
            return Institution_adm.objects.create(user=user) 
        else:
            return User.objects._create_user(**validated_data)
            Token.objects.create(user=user) 
