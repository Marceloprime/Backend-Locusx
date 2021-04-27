from django.urls import  path
from .views import *

urlpatterns = [
    path('', index ,name='index'),
    path('home/', home ,name='home'),
    path(r'singup/', singup ,name='singup'),
    path(r'institution/', Institution ,name='institution'),
]