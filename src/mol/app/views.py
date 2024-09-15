from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app/base.html')
    return HttpResponse(template.render())
