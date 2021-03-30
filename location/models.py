from django.db import models

from accounts.models import Teacher

class Location(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f'{self.name}: {self.latitude}, {self.longitude}'