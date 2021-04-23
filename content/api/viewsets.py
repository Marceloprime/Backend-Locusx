from content.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json
from content.api.serializers import *
from .permissions import *


class ContentViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ContentSerializers
  queryset = Content.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = QuestionSerializers
  queryset = Question.objects.all()

class OpenQuestionViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = OpenQuestionSerializers
  queryset = OpenQuestion.objects.all()

class AlternativeViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AlternativeSerializers
  queryset = Alternative.objects.all()

class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = MultipleChoiceQuestionSerializers
  queryset = MultipleChoiceQuestion.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = TaskSerializers
  queryset = Task.objects.all()

class ActivityTeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivityTeacherSerializers
  queryset = ActivityTeacher.objects.all()

class ActivityViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivitySerializers
  queryset = Activity.objects.all()

class ActivityRealizationViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivityRealizationSerializers
  queryset = ActivityRealization.objects.all()

class ActivityRealizationTeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivityRealizationTeacherSerializers
  queryset = ActivityRealizationTeacher.objects.none()

  def list(self, request):
    getUser = self.request.user

    if getUser.is_student == True:
      getStudent = Student.objects.filter(user=getUser).values_list('id', flat = True)[0]
      try:
        activities =  ActivityRealizationTeacher.objects.filter(student=getStudent)
        data = []

        for count in activities:
          aux = {
            "id" : count.id,
            "activity": str(count.activity),
            "activity_id": count.activity.id,
            "student": str(count.student),
            "student_id": count.student.id
          }
          data.append(aux)
      except:
        data = []

      return Response(data)
    else:
      return Response({"Data":[]})


class AnswerViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerSerializers
  queryset = Answer.objects.all()

class AnswerTeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerTeacherSerializers
  queryset = AnswerTeacher.objects.all()

class AnswerMultipleChoiceViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerMultipleChoiceSerializers
  queryset = AnswerMultipleChoice.objects.all()

class AnswerTeacherMultipleChoiceViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerTeacherMultipleChoiceSerializers
  queryset = AnswerTeacherMultipleChoice.objects.all()