from rest_framework import serializers, viewsets
from .models import PersonalNote


"""Describe the model and fields we want to use."""
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = PersonalNote 
    fields = ("title", "content")


"""Describe the rows we want from DB."""
class PersonalNoteViewSet(viewsets.ModelViewSet):
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.all()