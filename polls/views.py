from django.shortcuts import render
from django.http import HttpResponse

def index(result):
    return HttpResponse("polls index!")
