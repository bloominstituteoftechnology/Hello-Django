from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note): #I love inheritance with python!
  #this imports django's built in user class model
  user = models.ForeignKey(User, on_delete=models.CASCADE)
 #foreign key creates reference to data on another table
 #cascade helps with integrity of data TODO: look this up

 

