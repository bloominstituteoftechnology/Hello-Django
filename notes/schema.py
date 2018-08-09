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

    def mutate(self, info, title, content):
        user = info.context.user

        if user.is_anonymous:
            CreatePersonalNote(ok=False, status="Need to log in!")
        else:
            new_note = PersonalNoteModel(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personal_note=new_note, ok=True, content="Success!")

    

schema = graphene.Schema(query=Query)