from django.contrib import admin
from .models import Note
from .models import PersonalNote
# from .models import User
# Register your models here.

admin.site.register(Note)
admin.site.register(PersonalNote)
# admin.site.register(User)
