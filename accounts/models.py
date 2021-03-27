from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_institution_adm = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Student(models.Model):
    #username = models.ForeignKey(User, on_delete=models,related_name='usernames')
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Teacher(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Institution_adm(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email

class Institution(models.Model):
    user = models.ForeignKey('Institution_adm', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    teachers =  models.ManyToManyField(Teacher,blank=True)
    student =  models.ManyToManyField(Student,blank=True)
    def __str__(self):
        return self.name

class Address(models.Model):
    state = models.CharField(max_length=2)
    city = models.CharField( max_length=100)
    street = models.CharField( max_length=250)
    neighborhood = models.CharField( max_length=100)
    number = models.IntegerField()
    postal_code = models.CharField(max_length=250)
    complement = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
    )

    def __str__(self):
       return self.institution.name

###########################################################################
#                       Instituicao                                       #

class Program(models.Model):
    adm = models.ForeignKey('Institution_adm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    institution = models.ManyToManyField(Institution,blank=True)
    teachers =  models.ManyToManyField(Teacher,blank=True)
 
    def __str__(self):
        return self.name

class Class(models.Model):
    adm = models.ForeignKey('Institution_adm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="classes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    adm = models.ForeignKey('Institution_adm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    classes = models.ManyToManyField(Class)
    created_at = models.DateTimeField( auto_now_add=True)
    modified_at = models.DateTimeField( auto_now=True)
    teachers =  models.ManyToManyField(Teacher,blank=True)
  
    def __str__(self):
        return self.name

###########################################################################
#                       Teacher                                           #

class ProgramTeacher(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return self.name

class ClassTeacher(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    program = models.ForeignKey(
        ProgramTeacher,
        on_delete=models.CASCADE,
        related_name="classesteacher"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class CourseTeacher(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    classes = models.ManyToManyField(ClassTeacher)
    created_at = models.DateTimeField( auto_now_add=True)
    modified_at = models.DateTimeField( auto_now=True)
  
    def __str__(self):
        return self.name
###########################################################################