from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from notes.models import Note

# Create your views here.

def index(request):
    notes = Note.objects.order_by("-created_at")
    context = {
        'notes': notes,
    }
    return render(request, "notes/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def title_view(request, title):
    t = get_object_or_404(Note, title=title)
    return render(request, "notes/note.html", {'note': t})