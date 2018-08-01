from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
  """Describe the model and fields we want to use."""
  class Meta:
    model = PersonalNote
    fileds = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
  """Describe the rows we want from the DB."""

  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.all()