from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_app:list')