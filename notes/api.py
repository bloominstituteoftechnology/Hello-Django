from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        loggedInUser = self.context['request'].user
        note = PersonalNote.objects.create(user = loggedInUser, **validated_data)
        return note

    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer     
    queryset = PersonalNote.objects.all()
    def get_queryset(self):
        loggedInUser = self.request.user #how to get the user object
        anonUser = self.request.user.is_anonymous #t or f boolean
        if anonUser:
            return PersonalNote.object.none()
        else:
            return PersonalNote.objects.filter(user = loggedInUser)

