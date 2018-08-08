from graphene_django import DjangoObjectType
from graphene

from .models import PersonalNote as PersonalNoteModel

class PersonalNote(DjangoObjectType):

    class Meta:
        model = PersonalNoteModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    personalnotes = graphene.List(PersonalNote)

    def resolve_personalnotes(self, info):
        import pdb; pdb.set_trace()

schema = graphene.Schema(query=query)