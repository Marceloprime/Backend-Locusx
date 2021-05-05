"""locusx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
#from accounts.socialLogin import  FacebookLogin
from rest_framework import routers

from accounts.api.viewsets import *
from content.api.viewsets import *
from location.api.viewsets import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='LocusX API')
# Api router
router = routers.DefaultRouter()

#accounts
router.register(r'users', UserViewSet)
router.register(r'institution_adm', Institution_admViewSet, basename='Institution_adm')
router.register(r'teacher', TeacherViewSet, basename='Teacher')
router.register(r'student', StudentViewSet, basename='Student')
router.register(r'course', CourseViewSet, basename='Course')
router.register(r'programs', ProgramViewSet, basename='Program')
router.register(r'courseTeacher', CourseTeacherViewSet, basename='CourseTeacher')
router.register(r'programsTeacher', ProgramTeacherViewSet, basename='ProgramTeacher')
router.register(r'institution',InstitutionViewSet, basename='Institution')
router.register(r'class', ClassViewset, basename='Class')
router.register(r'classTeacher', ClassTeacherViewset, basename='ClassTeacher')

#content
router.register(r'content', ContentViewSet, basename='Content')
router.register(r'question', QuestionViewSet, basename='Question')
router.register(r'openquestion', OpenQuestionViewSet, basename='OpenQuestion')
router.register(r'alternative', AlternativeViewSet, basename='Alternative')
router.register(r'multiplechoicequestion', MultipleChoiceQuestionViewSet, basename='MultipleChoiceQuestion')
router.register(r'task', TaskViewSet, basename='Task')
router.register(r'activityTeacher', ActivityTeacherViewSet, basename='ActivityTeacher')
router.register(r'activity', ActivityViewSet, basename='Activity')
router.register(r'activityrealization', ActivityRealizationViewSet, basename='ActivityRealization')
router.register(r'activityrealizationteacher', ActivityRealizationTeacherViewSet, basename='ActivityRealizationTeacher')
router.register(r'answer', AnswerViewSet, basename='Answer')
router.register(r'answerteacher', AnswerTeacherViewSet, basename='AnswerTeacher')
router.register(r'answerMultipleChoice', AnswerMultipleChoiceViewSet, basename='AnswerMultipleChoice')
router.register(r'answerteacherMultipleChoice', AnswerTeacherMultipleChoiceViewSet, basename=' AnswerTeacherMultipleChoice')

#location
router.register(r'location', LocationViewSet, basename='LocationViewSet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('accounts.urls')),
    url(r'^auth/', include('rest_auth.urls')),#routar do login
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'docs/', schema_view)
]



#urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^signup', include('rest_auth.registration.urls')),
    #url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
#]
