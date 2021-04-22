from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Content)
admin.site.register(Question)
admin.site.register(OpenQuestion)
admin.site.register(Alternative)

admin.site.register(MultipleChoiceQuestion)
admin.site.register(Task)
admin.site.register(ActivityTeacher)
admin.site.register(Activity)

admin.site.register(ActivityRealization)
admin.site.register(ActivityRealizationTeacher)
admin.site.register(Answer)
admin.site.register(AnswerTeacher)
admin.site.register(AnswerMultipleChoice)
admin.site.register(AnswerTeacherMultipleChoice)