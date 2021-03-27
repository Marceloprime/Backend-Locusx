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

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'course', CourseViewSet, basename='Course')
router.register(r'programs', ProgramViewSet, basename='Program')
router.register(r'courseTeacher', CourseTeacherViewSet, basename='CourseTeacher')
router.register(r'programsTeacher', ProgramTeacherViewSet, basename='ProgramTeacher')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('site/', include('accounts.urls')),
    url(r'^auth/', include('rest_auth.urls')),#routar do login
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]



#urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^signup', include('rest_auth.registration.urls')),
    #url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
#]
