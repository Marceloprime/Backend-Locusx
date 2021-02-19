"""locusx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
#from accounts.socialLogin import  FacebookLogin
from rest_framework import routers
from accounts.api.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('site/', include('accounts.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]



#urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^signup', include('rest_auth.registration.urls')),
    #url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
#]
