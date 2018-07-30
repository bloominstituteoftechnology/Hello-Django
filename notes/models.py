from django.db import models
from uuid import uuid4

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # Unique ID
    username = models.CharField(max_length=200, unique=True) # one string no bigger than 200 chars
    password = models.CharField(max_length=200) # one string no bigger than 200 chars

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # Unique ID
    title = models.CharField(max_length=200) # one string no bigger than 200 chars
    content = models.TextField(blank=True) # a text block as big as it permits: can be empty
    created_at = models.DateTimeField(auto_now_add=True) # like Date.now() automatically calculated on creation
    last_modified = models.DateTimeField(auto_now=True) # When it was last edited auto calculater
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If the Refference gets deleted, it will clear the author field.

# Create your models here.
