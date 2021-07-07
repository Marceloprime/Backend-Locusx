from django.urls import  path, include
from .views import *
from location.views import LocationView
from content.views import *

urlpatterns = [
    path('', index ,name='index'),
    path('logout/',logout_view,name='logout'),
    path('home/', home ,name='home'),
    path(r'singup/', singup ,name='singup'),
    path(r'institution/', InstitutionView ,name='institution'),
    path(r'address/', AddressView ,name='address'),
    path(r'program/', ProgramView ,name='program'),
    path(r'class/', ClassView ,name='class'),
    path(r'course/', CourseView ,name='course'),
    path(r'programTeacher/', ProgramTeacherView ,name='programTeacher'),
    path(r'classTeacher/', ClassTeacherView ,name='classTeacher'),
    path(r'CreateclassTeacher/', CreateclassTeacherView ,name='CreateclassTeacher'),
    path(r'courseTeacher/', CourseTeacherView ,name='courseTeacher'),

    #location
    path(r'location/', LocationView ,name='location'),

    #Content
    path(r'content/', ContentView ,name='content'),
    path(r'question/', QuestionView ,name='question'),
    path(r'openQuestion/', OpenQuestionView ,name='openQuestion'),
    path(r'alternative/', AlternativeView ,name='alternative'),
    path(r'multipleChoiceQuestion/', MultipleChoiceQuestionView ,name='multipleChoiceQuestion'),  
    path(r'task/', TaskView ,name='task'),    
    path(r'activityTeacher/', ActivityTeacherView ,name='activityTeacher'),    
    path(r'activity/', ActivityView ,name='activity'),   
    path(r'activityRealization/', ActivityRealizationView ,name='activityRealization'),    
    path(r'activityRealizationTeacher/', ActivityRealizationTeacherView ,name='activityRealizationTeacher'), 
    path(r'answer/', AnswerView ,name='answer'),  
    path(r'answerTeacher/', AnswerTeacherView ,name='answerTeacher'), 
    path(r'answerMultipleChoice/', AnswerMultipleChoiceView ,name='answerMultipleChoice'), 
    path(r'answerTeacherMultipleChoice/', AnswerTeacherMultipleChoiceView ,name='answerTeacherMultipleChoice'), 

    path('accounts/', include('allauth.urls')),
]