from django.contrib import admin
from .models import User, Teacher, Student, Institution_adm, Institution, Address, Program, Class, Course

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