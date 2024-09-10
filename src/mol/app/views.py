from django.shortcuts import render
from . import urls
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")