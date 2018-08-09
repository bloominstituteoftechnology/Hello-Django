rom graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel 

class PersonalNote(DjangoObjectType):
    """Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalNoteModel

        interface = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    """Describe which records we want to show."""
    notes = graphene.List(Note)

    def resolve_notes(self, info):
        """Decide what notes to return."""
        pass # TODO