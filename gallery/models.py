from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Gallery(models.Model):
    image = models.URLField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
