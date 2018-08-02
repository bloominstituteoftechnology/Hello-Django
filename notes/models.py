from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return self.title[:50]

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)