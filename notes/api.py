from rest_framework import serializers, viewsets
from .models imort PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkModelSerializers):
    """Describe the model and fields we want to use"""

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PerosnalNotViewSet(viewsets.ModelViewSet):
    """Describe the rows we want from the DB"""

    serializer_class = PersonalNoteSerializer
    queryset = PerosnalNote.objects.all()


