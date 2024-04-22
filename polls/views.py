from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(req):
    question_list = Question.objects.order_by("-publish_date")[:5]
    return render(req, "polls/index.html", {"question_list": question_list})

def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})

def results(req, question_id):
    response = "Here's the result of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
