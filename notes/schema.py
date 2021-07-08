from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel

# --- query stuff ---

class PersonalNote(DjangoObjectType):

  class Meta:
    model = PersonalNoteModel
    # Describe the data as a node in the graph
    interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
  personalnotes = graphene.List(PersonalNote)

  def resolve_personalnotes(self, info):
    """Decide which notes to return."""
    
    user = info.context.user # Find with debugger

    if user.is_anonymous:
      return PresonalNoteModel.object.none()
    else:
      return PersonalNoteModel.objects.filter(user = user)

# --- mutation stuff ---
    
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
      return CreatePersonalNote(ok = False, status = "Must be loggen in!")
    else:
      new_note = PersonalNoteModel(title = title, content = content, user = user)
      new_note.save()
      return CreatePersonalNote(personalnote = new_note, ok = True, status = "ok")
    
class Mutation(graphene.ObjectType):
  create_personal_note = CreatePersonalNote.Field()


schema = graphene.Schema(query = Query, mutation = Mutation)
