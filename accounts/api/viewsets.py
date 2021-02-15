from accounts.models import  User, Teacher, Student, Institution_adm, Institution, Address, Program, Class, Course
from rest_framework import viewsets
from rest_framework import permissions
from accounts.api.serializers import  UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]