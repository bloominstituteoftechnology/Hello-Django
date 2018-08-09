from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipCode = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.firstName + " " + self.lastName


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
