from django.db import models
from uuid import uuid4

# Create your models here.

class Notes(models.Model):
    id = models.UUIDField()
    title = models.CharField()
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()