from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Institution_adm)
admin.site.register(Institution)
admin.site.register(Address)
admin.site.register(Program)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(ProgramTeacher)
admin.site.register(ClassTeacher)
admin.site.register(CourseTeacher)

admin.site.unregister(Group)

#customization
admin.site.site_header = "LocusX"
admin.site.site_title = "Administração"
admin.site.index_title = "LocusX"