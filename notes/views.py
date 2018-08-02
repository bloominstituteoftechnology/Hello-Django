from .models import PersonalNote
from rest_framework import viewsets
from .api import PersonalNoteSerializer

class PersonalNoteViewSet(viewsets.ModelViewSet):
	serializer_class = PersonalNoteSerializer
	queryset = PersonalNote.objects.none()

	def create(self, validated_data):
		# import pdb; pdb.set_trace()
		user = self.context['request'].user
		note = PersonalNote.objects.create(user=user, **validated_data)
		return note

	def get_queryset(self):
		# import pdb; pdb.set_trace()
		user = self.request.user

		if user.is_anonymous:
			return PersonalNote.objects.none()
		else:
			return PersonalNote.objects.filter(user=user)