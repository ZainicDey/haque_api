from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()