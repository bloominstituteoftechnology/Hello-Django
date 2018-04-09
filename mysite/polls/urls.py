from django.urls import path

From . import views

urlpattern = [
    path('', views.index, name = 'index'),
     ]