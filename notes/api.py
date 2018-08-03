from rest_framework import serializers

class PersonalNoteSerializer(serializers.HyperLinkedModelSerializer):

    class Meta:
      model = PersonalNote
      fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
  #describe the rows we want from the db
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.all()