from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(result):
    question_list = Question.objects.order_by("-pub_date")[:5]
    response = ", ".join([q.question_text for q in question_list])
    return HttpResponse(response)

def detail(req, question_id):
    return HttpResponse("Question number %s." %question_id)

def results(req, question_id):
    response = "Here's the result of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
