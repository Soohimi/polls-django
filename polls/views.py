from django.shortcuts import render
from django.http import HttpResponse,Http404

from .models import Question


def index(req):
    question_list = Question.objects.order_by("-publish_date")[:5]
    return render(req, "polls/index.html", {"question_list": question_list})

def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")    
    return render(req, "polls/detail.html",{"question":question})

def results(req, question_id):
    response = "Here's the result of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
