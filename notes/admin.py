from django.contrib import admin

# Register your models here.
from .models import Question, Note, PersonalNote

admin.site.register(Question)
admin.site.register(Note)
admin.site.register(PersonalNote)
