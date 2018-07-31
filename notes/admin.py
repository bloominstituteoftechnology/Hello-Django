from django.contrib import admin

# Register your models here.

from .models import Note
admin.site.register(Note)

from .models import PersonalNote
admin.site.register(PersonalNote)