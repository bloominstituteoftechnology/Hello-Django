from graphene_django import DjangoObjectType
import graphene

from .models import PersonalNote as PersonalNoteModel

class PersonalNote(DjangoObjectType):

    class Meta:
        model = PersonalNoteModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    personalnotes = graphene.List(PersonalNote)

    def resolve_personalnotes(self, info):
        # import pdb; pdb.set_trace()
        user = info.context.user

        if user.is_anonymous:
            return PersonalNoteModel.objects.none()
        else:
            return PersonalNoteModel.objects.filter(user=user)

class CreatePersonalNote(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()
    
    personalnote = graphene.Field(PersonalNote)
    ok = graphene.Boolean()
    status = graphene.String()

    

schema = graphene.Schema(query=Query)