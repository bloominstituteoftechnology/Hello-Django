from django.db import models
from uuid import uuid4

class Note(models.Model):
    id = models.UUIDField(primary_key =True,default=uuid4,editable=False)
    title = models.CharField(max_length= 200)
    content = models.TextField(blank= 200)
    created_at = models.DateTimeField(auto_now_add= 200)
    last_modified = models.DateTimeField(auto_now= 200)