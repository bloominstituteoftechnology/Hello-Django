from django.contrib import admin
from .models import Note, PersonalNote

# Register your models here.
admin.site.register((Note, PersonalNote)) # in double perens b/c is a tuple-ype of arr 