from rest_framework import serializers, viewsets
from notes.models import PersonalNote

# ModelName+Serializer(inherits) Describes the model and fields we want to use
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'url')

    # OverWrite Create: Which gets called on post of a new note in django's interface
    # Figure out how to inject the currently logged in user to it.
    def create(self, validated_data):
        loggedInUser = self.context['request'].user
        note = PersonalNote.objects.create(user=loggedInUser,**validated_data)
        return note

# Describe the rows we want from the DB
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

    def get_queryset(self):
        loggedInUser = self.request.user
        # print(loggedInUser)
        # import pdb; pdb.set_trace()  # Start the debugger here
        anonUser = loggedInUser.is_anonymous
        # return PersonalNote.objects.all()
        # FIGURE OUT WHY USER STILL IS ANON WHEN PROVIDING THE RIGHT TOKEN???
        if anonUser:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=loggedInUser)