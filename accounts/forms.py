from django import forms
from django.core.mail import  EmailMessage
from .models import *

class InstitutionModelForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'

class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class ProgramModelForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class ClassModelForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class ProgramTeacherModelForm(forms.ModelForm):
    class Meta:
        model = ProgramTeacher
        fields = '__all__'

class ClassTeacherModelForm(forms.ModelForm):
    class Meta:
        model = ClassTeacher
        fields = '__all__'

class CourseTeacherModelForm(forms.ModelForm):
    class Meta:
        model = CourseTeacher
        fields = '__all__'
