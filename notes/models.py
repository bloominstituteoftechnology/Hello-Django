from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
class Note(models.Model):
    id = models.UUIDField(primary_key =True,default=uuid4,editable=False)
    title = models.CharField(max_length= 200)
    content = models.TextField(blank= 200)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add= 200)
    last_modified = models.DateTimeField(auto_now= 200)
 

class PersonalNote(Note):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    