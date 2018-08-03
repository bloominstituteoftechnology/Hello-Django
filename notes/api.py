from rest_framework import serializers, viewsets

from .models import Note
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url','id')

    def create(self, validated_data):
        user = self.context['request'].user
        # import pdb; pdb.set_trace()
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    # queryset = PersonalNote.objects.all()
    queryset = Note.objects.none() 

    def get_queryset(self):
        user = self.request.user

        # if user.is_anonymous:
        #     print("i got in annonmyous")
        #     return PersonalNote.objects.none()
        # else:
        print("i got in not annonmyous")
        return PersonalNote.objects.filter(user=user)