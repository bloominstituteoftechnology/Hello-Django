from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from rest_framework.authtoken import views
from notes.api import NoteViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^api-token-auth/', views.obtain_auth_token)
]
