from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "question_list": question_list,
    }
    return HttpResponse(template.render(context,request))

def detail(req, question_id):
    return HttpResponse("Question number %s." %question_id)

def results(req, question_id):
    response = "Here's the result of question %s."
    return HttpResponse(response % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
