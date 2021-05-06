import os
import hashlib

from time import time

from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import *
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
    belongs_to_an_institution = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(_('description'), blank=True, null=True)
    is_openQuestion = models.BooleanField(default=False)
    is_multipleChoiceQuestion = models.BooleanField(default=False)
    link_multimedia = models.TextField(_('link multimedia'), blank=True, null=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="question",
        null=True
    )

    def __str__(self):
        return self.title

class OpenQuestion(models.Model):
    question  = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="openquestion",
        null=True
    )
    suggestionOfCorrectAnswer = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.question.title        

class Alternative(models.Model):
    question  = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="Alternative",
        null=True
    )
    letter =  models.TextField(_('letter'), blank=False)
    description = models.TextField(_('description'))
    
    def __str__(self):
        return self.letter


class MultipleChoiceQuestion(models.Model):
    question  = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="multipleChoiceQuestion",
        null=True
    )

    alternative = models.ManyToManyField(Alternative, verbose_name="alternative")

    def __str__(self):
        return self.question.title        

class Task(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    description = models.TextField(_('description'), blank=True, null=True)
    questions = models.ManyToManyField(Question, verbose_name="question")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="taks_location", null=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="task",
        null=True
    )
    def __str__(self):
        return self.title

class ActivityTeacher(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(_('description'), blank=True, null=True)
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name="activitiesTeacher"
    )
    course = models.ForeignKey(
        CourseTeacher,
        on_delete=models.CASCADE,
        related_name="activitiesTeacher",
        null=True
    )
    class_id = models.ForeignKey(
        ClassTeacher,
        on_delete=models.CASCADE,
        related_name="activitiesTeacher",
        null=True
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="activitiesTeacher",
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    taks = models.ManyToManyField(Task, verbose_name="taks")
    belongs_to_an_institution = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(_('description'), blank=True, null=True)
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name="activitiesContent"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="activitiesCourse",
        null=True
    )
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="activitiesClass",
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    taks = models.ManyToManyField(Task, verbose_name="taks")
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="activities",
        null=True
    )
    belongs_to_an_institution = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ActivityRealization(models.Model):
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
        return f'{self.student.user.email}: {self.activity.title}'

class ActivityRealizationTeacher(models.Model):
    activity = models.ForeignKey(
        ActivityTeacher,
        on_delete=models.CASCADE,
        related_name="ActivityRealizationTeacher"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="ActivityRealizationTeacher"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ActivityRealizationTeacher'

    def __str__(self):
        return f'{self.student.user.email}: {self.activity.title}'
    
class Answer(models.Model):
    answer = models.TextField(_('description'), blank=True, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=2, default=0)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="Answer"
    )
    activityRealization = models.ForeignKey(
        ActivityRealization,
        on_delete=models.CASCADE,
        related_name="Answer"
    )

class AnswerTeacher(models.Model):
    answer = models.TextField(_('description'), blank=True, null=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="AnswerTeacher"
    )
    activityRealization = models.ForeignKey(
        ActivityRealizationTeacher,
        on_delete=models.CASCADE,
        related_name="AnswerTeacher"
    )


class AnswerMultipleChoice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="AnswerMultipleChoice"
    )
    alternative = models.ForeignKey(
        Alternative,
        on_delete=models.CASCADE,
        related_name="AnswerMultipleChoice"
    )
    activityRealization = models.ForeignKey(
        ActivityRealization,
        on_delete=models.CASCADE,
        related_name="AnswerMultipleChoice"
    )

class AnswerTeacherMultipleChoice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="AnswerTeacherMultipleChoice"
    )

    alternative = models.ForeignKey(
        Alternative,
        on_delete=models.CASCADE,
        related_name="AnswerTeacherMultipleChoice"
    )
    activityRealization = models.ForeignKey(
        ActivityRealizationTeacher,
        on_delete=models.CASCADE,
        related_name="AnswerTeacherMultipleChoice"
    )
