from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel

# https://github.com/fmarkwong-lambda-school-cs9-coursework/GraphQL/blob/master/guides/day1.md
class PersonalNote(DjangoObjectType):
    """Describe which model we want to expose through GraphQL"""
    class Meta:
        model = PersonalNoteModel
        # Describe data as a node in for GraphQL
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    # personalnotes will be the graphql query term to use
    # e.g.  
    # {
    #   personalnotes {
    #     title
    #     content
    #     lastModified
    #   }
    # }
    personalnotes = graphene.List(PersonalNote)

    # name of this function should match the personalnotes var above
    def resolve_personalnotes(self, info):
        """Decide which rows we want from the DB"""
        user = info.context.user # Find this with debugger
        # import pdb; pdb.set_trace()

        if user.is_anonymous:
            return PersonalNoteModel.objects.none()
        else:
            # return PersonalNoteModel.objects.filter(user=user)
            return PersonalNoteModel.objects.filter(user=user)

schema = graphene.Schema(query=Query)
