from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel

# Query Stuff


class PersonalNote(DjangoObjectType):

    class Meta:
        model = PersonalNoteModel
        # Describe the data as a node in the graph
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    notes = graphene.List(PersonalNote)

    def resolve_notes(self, info):
        """Decide which notes to return."""

        user = info.context.user
        if user.is_anonymous:
            return PersonalNoteModel.objects.none()
        else:
            return PersonalNoteModel.objects.filter(user=user)

# Mutation Stuff


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
            return CreatePersonalNote(ok=False, status="Not signed in!")
        else:
            new_note = PersonalNoteModel(
                title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="Perfect.")


class Mutation(graphene.ObjectType):
    create_personal_note = CreatePersonalNote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
