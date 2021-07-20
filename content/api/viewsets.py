from content.models import *
from accounts.models import *
from location.models import *
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
  queryset = Content.objects.all()# até o momento não há problemas em deixa isso aberto

  @action(methods=['get'],detail=False)
  def get_Content(self, request):
    getUser = self.request.user
    getTeacher = Teacher.objects.filter(user=getUser).values_list('id', flat = True)[0]
    contents = Content.objects.filter(teacher=getTeacher)
    data = []

    for content in contents:
      
      aux = {
        "name" : content.title,
        "description" : content.description
      }

      data.append(aux)
      
    return Response(data)

class QuestionViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = QuestionSerializers
  queryset = Question.objects.all()

  @action(methods=['get'],detail=False)
  def get_Question(self, request):
    getUser = self.request.user
    getTeacher = Teacher.objects.filter(user=getUser).values_list('id', flat = True)[0]
    questions =  Question.objects.filter(teacher=getTeacher)
    data = []
    alternatives = []

    for question in questions:
      multipleChoiceQuestions = Alternative.objects.filter(question=question.id)

      for multipleChoiceQuestion in multipleChoiceQuestions:
        collect = {
          "id": multipleChoiceQuestion.id,
          "letter": multipleChoiceQuestion.letter,
          "description": multipleChoiceQuestion.description,
        }
        alternatives.append(collect)
      alternatives = json.dumps(alternatives)
      aux = {
        "id": question.id,
        "title": question.title,
        "description": question.description,
        "is_openQuestion": question.is_openQuestion,
        "is_multipleChoiceQuestion": question.is_multipleChoiceQuestion,
        "link_multimedia": question.link_multimedia,
        "alternatives": alternatives
      }

      data.append(aux)
    return Response(data)

class OpenQuestionViewSet(viewsets.ModelViewSet):#OK
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = OpenQuestionSerializers
  queryset = OpenQuestion.objects.all()

class AlternativeViewSet(viewsets.ModelViewSet):#OK
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AlternativeSerializers
  queryset = Alternative.objects.all()

class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = MultipleChoiceQuestionSerializers
  queryset = MultipleChoiceQuestion.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = TaskSerializers
  queryset = Task.objects.all()

  @action(methods=['get'],detail=False)
  def get_TaskStudent(self, request):
    getUser = self.request.user
    getStudent = Student.objects.filter(user=getUser).values_list('id', flat = True)[0]
    classes = Class.objects.filter(students=getStudent).values_list('teachers', flat = True)[0]
    getTeacher = Teacher.objects.filter(id=classes).values_list('id', flat = True)[0]
    getTasks = Task.objects.filter(teacher=getTeacher)
   
    data = []
 

    for task in getTasks:
      if task.status == False:
        continue

      questions = Task.objects.get(id=task.id).questions.all()
      questionData = []
      for question in questions:

        multipleChoiceQuestions = Alternative.objects.filter(question=question.id)
        alternatives = []
        for multipleChoiceQuestion in multipleChoiceQuestions:
          collect = {
            "id": str(multipleChoiceQuestion.id),
            "letter": str(multipleChoiceQuestion.letter),
            "description":str(multipleChoiceQuestion.description),
          }
          alternatives.append(collect)

        aux = {
          "id": question.id,
          "title": question.title,
          "description": question.description,
          "is_openQuestion": question.is_openQuestion,
          "is_multipleChoiceQuestion": question.is_multipleChoiceQuestion,
          "link_multimedia": question.link_multimedia,
          "alternatives": alternatives
        }

        questionData.append(aux)
      questionData = json.dumps(questionData, ensure_ascii=False).encode('utf8')
      aux = {
        "title" : task.title,
        "description" : task.description,
        "questions" : questionData,
        "location":str({
          "id": str(task.location.id),
          "name": str(task.location.name),
          "description": str(task.location.description),
          "latitude": str(task.location.latitude),
          "longitude": str(task.location.longitude),
        })
      }
      
      data.append(aux)
    return Response(data)

class ActivityTeacherViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivityTeacherSerializers
  queryset = ActivityTeacher.objects.all()

  @action(methods=['get'],detail=False)
  def get_student_activity(self,request):
    data = []
    dataAux = []
    if request.user.is_student:
      getUser = request.user
      getStudent = Student.objects.filter(user=getUser).values_list('id', flat = True)[0]
      classes = ClassTeacher.objects.filter(students=getStudent)
      for class_ in classes:
        activities = ActivityTeacher.objects.filter(class_id=class_.id)#atividades por classe
        for activity in activities:#Busca em cada atividade
          tasks = activity.tasks.all()#todas as tarefas por classe         
          for task in tasks:
            print(activity)
            print(task.title)
            print('\n\n')

            if task.status == False:#caso a tarefa ja tenha sido feita
              continue

            questions = Task.objects.get(id=task.id).questions.all()
            questionData = []
            for question in questions:

              multipleChoiceQuestions = Alternative.objects.filter(question=question.id)
              alternatives = []
              for multipleChoiceQuestion in multipleChoiceQuestions:
                collect = {
                  "id": str(multipleChoiceQuestion.id),
                  "letter": str(multipleChoiceQuestion.letter),
                  "description":str(multipleChoiceQuestion.description),
                }
                alternatives.append(collect)

              aux = {
                "id": str(question.id),
                "title": str(question.title),
                "description": str(question.description),
                "is_openQuestion": str(question.is_openQuestion),
                "is_multipleChoiceQuestion": str(question.is_multipleChoiceQuestion),
                "link_multimedia": str(question.link_multimedia),
                "alternatives": alternatives
              }

              questionData.append(aux)
            aux = {
              "title" : str(task.title),
              "description" : str(task.description),
              "questions" : questionData,
              "location":str({
                "id": str(task.location.id),
                "name": str(task.location.name),
                "description": str(task.location.description),
                "latitude": str(task.location.latitude),
                "longitude": str(task.location.longitude),
              })
            }
            
            dataAux.append(aux)

          #print(dataAux)  
          #print("\n\n\n") 
          data.append({
            "id": activity.id,
            "name" : activity.title,
            "class" : class_.name,
            "tasks": str(dataAux)
          })
          dataAux = []
      #print(data)
      return Response({"data": data})
    else:
      return Response({"message": "Você não está autorizado para essa requisição."})
class ActivityViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivitySerializers
  queryset = Activity.objects.all()

class ActivityRealizationViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivityRealizationSerializers
  queryset = ActivityRealization.objects.all()

class ActivityRealizationTeacherViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = ActivityRealizationTeacherSerializers
  queryset = ActivityRealizationTeacher.objects.all()

  @action(methods=['get'],detail=False)
  def get_ActivityRealizationTeacher(self, request):
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
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerSerializers
  queryset = Answer.objects.all()

class AnswerTeacherViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerTeacherSerializers
  queryset = AnswerTeacher.objects.all()

class AnswerMultipleChoiceViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerMultipleChoiceSerializers
  queryset = AnswerMultipleChoice.objects.all()

class AnswerTeacherMultipleChoiceViewSet(viewsets.ModelViewSet):
  #permission_classes = [permissions.IsAuthenticated]
  serializer_class = AnswerTeacherMultipleChoiceSerializers
  queryset = AnswerTeacherMultipleChoice.objects.all()