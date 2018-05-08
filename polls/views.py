# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# import the Question model
from .models import Question
""" common pattern: load a template, fill in the context, and return HttpRes 
with result of rendered template. But with django shortcuts and render()
the code can be cut down considerably
"""
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)
  # template = loader.get_template('polls/index.html')
  # return HttpResponse(template.render(context, request))
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)
  # return HttpResponse("Hello, world. You're at the polls index")

def detail(request, question_id):
  # return render(request, )
  return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)


