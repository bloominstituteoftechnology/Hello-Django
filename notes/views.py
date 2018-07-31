from django.template import loader
from django.http import HttpResponse
from notes.models import PersonalNote
# Create your views here.
def notes(request):
    notesList = PersonalNote.objects.all()
    template = loader.get_template("notes.html")
    context = {
        "notes": notesList,
        "styles": [{"color": "red"}, {"color": "blue"}, {"color": "purple"}] #tried to give each one its own color but stil have to figure out the correct syntax
    }
    return HttpResponse(template.render(context, request))
