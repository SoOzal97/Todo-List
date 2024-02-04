from django.db import models

# Create your models here.
class Task(models.Model):
    title= models.CharField( max_length=50)
    description = models.TextField()
    status=models.BooleanField(default=False)
