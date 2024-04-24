from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic

from .models import Question,Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name="question_list"

    def get_queryset(self):
        return Question.objects.order_by("-publish_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"        

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
