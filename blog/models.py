from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.title