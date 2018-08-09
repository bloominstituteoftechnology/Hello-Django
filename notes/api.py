from rest_framework import serializers, viewsets
from .models import PersonalNote



class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
  # title and content 


      def create( self, validated_data):
        #   import pdb; pdb.set_trace()
          user = self.context['request'].user
          note = PersonalNote.objects.create(user=user,**validated_data)
          return note


      class Meta:
              model = PersonalNote
              fields = ("title",'content', 'url', 'id')


class PersonalNoteViewSet(viewsets.ModelViewSet):
  # rows we want from DB
      serializer_class = PersonalNoteSerializer
      queryset = PersonalNote.objects.none()
      #queryset = PersonalNote.objects.none()
      def get_queryset(self):
            # import pdb; pdb.set_trace()
            user = self.request.user
            
            if user.is_anonymous:
                return PersonalNote.objects.none()
            elif user.is_superuser:
                return PersonalNote.objects.all()
            else:
                return PersonalNote.objects.filter(user=user)
            