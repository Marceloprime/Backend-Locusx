from django.db import models
from django.utils.translation import  gettext_lazy as _

from accounts.models import Teacher

class Location(models.Model):
    name = models.CharField(_('name'),max_length=250)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    description = models.TextField(_('description'),blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f'{self.name}: {self.latitude}, {self.longitude}'