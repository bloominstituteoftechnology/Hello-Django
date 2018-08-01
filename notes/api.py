from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validate_data)
        return note 

    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    """Describe the rows we want from the DB."""
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none() #change none to all and you will see all user notes

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else: 
            return PersonalNote.objects.filter(user=user) # you can use lots of different filters here 
            