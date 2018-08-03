from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='notestorage')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title + "|" + self.content


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
