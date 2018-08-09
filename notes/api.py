from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    """Describe the model and fields we want to use."""

    def create(self, validated_data):
        note = PersonalNote.object.create(**validated - data)
        return note

    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    """Describe the rows we want from the DB."""

    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
