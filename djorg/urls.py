
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from notes.api import PersonalNoteViewSet


router = routers.DefaultRouter()
router.register('notes', PersonalNoteViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))

]
