from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    completion = models.BooleanField(blank=True, default=False, null=True)


    def __str__(self):
        return self.title