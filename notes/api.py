from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # import pdb; pdb.set_trace() 
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note
        
    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    # Describe rows we want from the Database
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

    def get_queryset(self):
        # specify the types of querysets you want to pull - all user items
        # import pdb; pdb.set_trace() <- debugger that allows for code checking
        user = self.request.user

        if user.is_anonymous: # django default
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
            