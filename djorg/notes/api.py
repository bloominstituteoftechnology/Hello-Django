from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewset(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
    