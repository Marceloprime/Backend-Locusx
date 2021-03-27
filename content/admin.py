from django.contrib import admin
from .models import Activity, Content, ActivityAnswer, Task, GenericsQuestion
# Register your models here.
admin.site.register(Activity)
admin.site.register(Content)
admin.site.register(ActivityAnswer)
admin.site.register(Task)
admin.site.register(GenericsQuestion)