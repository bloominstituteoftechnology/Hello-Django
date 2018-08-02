from rest_framework import serializers
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
	# inner class - tells which data to access
	class Meta:
		model = PersonalNote
		fields = ('title', 'content')


