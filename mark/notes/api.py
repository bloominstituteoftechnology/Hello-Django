from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    """DESCRIBE THE MODEL AND FIELDS WE WANT TO USE"""
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    """Describe the rows we want from the DB"""

    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()