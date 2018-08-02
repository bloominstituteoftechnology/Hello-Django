from rest_framework import serializers
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
	# inner class - tells which data to access
	class Meta:
		model = PersonalNote
		fields = ('title', 'content')

	def create(self, validated_data):
		# import pdb; pdb.set_trace()
		user = self.context['request'].user
		note = PersonalNote.objects.create(user=user, **validated_data)
		return note

	
