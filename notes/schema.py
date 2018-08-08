from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel

class PersonalNote(DjangoObjectType):
    
    class Meta:
        model = PersonalNoteModel
        interfaces = (graphene.relay.Node,)
        # Describe the data as a node in the graph

class Query(graphene.ObjectType):
    notes = graphene.List(PersonalNote)

    def resolve_notes(self, info):
        """Decide which notes to return."""
        user = info.context.user #Find with debugger

        if user.is_anonymous:
            return PersonalNoteModel.objects.none()
        elif user.is_superuser:
            return PersonalNoteModel.objects.all()
        else:
            return PersonalNoteModel.objects.filter(user=user)
        
schema = graphene.Schema(query=Query)