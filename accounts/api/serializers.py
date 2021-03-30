from rest_framework import serializers
from accounts.models import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    is_active = serializers.BooleanField(default=True,write_only=True)
    is_student = serializers.BooleanField(default=False,write_only=True)
    is_teacher = serializers.BooleanField(default=False,write_only=True)
    is_institution_adm = serializers.BooleanField(default=False,write_only=True)

    def create(self, validated_data):
        is_student = validated_data.get('is_student')
        is_teacher = validated_data.get('is_teacher')
        is_institution_adm = validated_data.get('is_institution_adm')
        emailinfo = validated_data.get('email')
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

class Institution_admSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institution_adm
        fields = '__all__'

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

#seriealizers da intituicao
#######################################################################
class ClassSerializers(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):
    classes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['adm','name','description','classes','name','description']

class ProgramSerializers(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
#######################################################################
#seriealizers do professor
#######################################################################
class ClassTeacherSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClassTeacher
        fields = '__all__'

class CourseTeacherSerializers(serializers.ModelSerializer):
    classes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = CourseTeacher
        fields =  '__all__'

class ProgramTeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProgramTeacher
        fields = '__all__'
#######################################################################
class InstitutionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'