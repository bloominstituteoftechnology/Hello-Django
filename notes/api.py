from rest_framework import serializers, viewsets
from .models import PersonalNote


"""Describe the model and fields we want to use."""
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

  def create(self, validated_data):
    # import pdb; pdb.set_trace() # invoke debugger
    user = self.context["request"].user
    note = PersonalNote.objects.create(user=user, **validated_data)
    return note

  class Meta:
    model = PersonalNote 
    fields = ("title", "content")


"""Describe the rows we want from DB."""
class PersonalNoteViewSet(viewsets.ModelViewSet):
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.none()

  def get_queryset(self):
    # import pdb; pdb.set_trace()
    user = self.request.user

    if user.is_anonymous:
      return PersonalNote.objects.none()
    else:
      return PersonalNote.objects.filter(user=user)
