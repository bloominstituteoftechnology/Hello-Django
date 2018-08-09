
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers 
from notes.api import PersonalNoteViewSet
from rest_framework.authtoken import views 

from graphene_django.views import GraphQLView

router = routers.DefaultRouter()
router.register('notes', PersonalNoteViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('^api-token-auth/', views.obtain_auth_token),
    path('graphQL/', GraphQLView.as_view(graphiql=True)),
]
