from django import forms
from django.core.mail import  EmailMessage
from .models import *

class LocationModelForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'