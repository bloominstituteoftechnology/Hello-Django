
from django.urls import path
from . import views

# path(views) is ''...blank cos in urls.py(djorg folder)..we already have 'bookmarks/'....the '' here means nothing after the url 'bookmarks/'
urlpatterns = [
  path('', views.index, name='index')
]