from django.shortcuts import render
from django.http import HttpResponse

def index(result):
    return HttpResponse("polls index!")

def detail(req, question_id):
    return HttpResponse("Question number %s." %question_id)

def results(req, question_id):
    response = "Here's the result of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
