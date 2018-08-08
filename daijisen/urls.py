from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.index, name='index'),
    path('word/<word>', cache_page(60 * 15)(views.word), name='word')
]
