import os
import hashlib

from time import time

from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Teacher, Student, Course, Class
from location.models import Location



class Content(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(_('description'), blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="contents",
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class GenericsQuestion(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(_('description'), blank=True, null=True)
    taks = models.ManyToManyField(GenericsQuestion, verbose_name="question")

    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(_('description'), blank=True, null=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="activities"
    )
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name="activities"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="activities",
        null=True
    )
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="activities",
        null=True
    )
    multimedia_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    taks = models.ManyToManyField(Task, verbose_name="taks")


    def __str__(self):
        return self.title


class ActivityAnswer(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activity_answer'

    def __str__(self):
        return f'{self.student.full_name}: {self.google_drive_file_key}'