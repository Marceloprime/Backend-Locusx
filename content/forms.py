from django import forms
from django.core.mail import  EmailMessage
from .models import *

class ContentModelForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
class OpenQuestionModelForm(forms.ModelForm):
    class Meta:
        model = OpenQuestion
        fields = '__all__'

class AlternativeModelForm(forms.ModelForm):
    class Meta:
        model = Alternative
        fields = '__all__'

class MultipleChoiceQuestionModelForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = '__all__'

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class ActivityTeacherModelForm(forms.ModelForm):
    class Meta:
        model = ActivityTeacher
        fields = '__all__'

class ActivityModelForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'

class ActivityRealizationModelForm(forms.ModelForm):
    class Meta:
        model = ActivityRealization
        fields = '__all__'

class ActivityRealizationTeacherModelForm(forms.ModelForm):
    class Meta:
        model = ActivityRealizationTeacher
        fields = '__all__'

class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

class AnswerTeacherModelForm(forms.ModelForm):
    class Meta:
        model = AnswerTeacher
        fields = '__all__'

class AnswerMultipleChoiceModelForm(forms.ModelForm):
    class Meta:
        model = AnswerMultipleChoice
        fields = '__all__'

class AnswerTeacherMultipleChoiceModelForm(forms.ModelForm):
    class Meta:
        model = AnswerTeacherMultipleChoice
        fields = '__all__'
