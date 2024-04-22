from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

from .models import Question,Choice


def index(req):
    question_list = Question.objects.order_by("-publish_date")[:5]
    return render(req, "polls/index.html", {"question_list": question_list})

def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", {"question": question})

def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/results.html", {"question":question})


def vote(req, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(req,"polls/detail.html",
                      {"question": question,"error_message": "You did not select a choice!",},
                    )  
    else:
        selected_choice.votes=F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))  
