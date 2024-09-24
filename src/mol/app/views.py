from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader
import csv

def get_questions(id): # Hakkab lugema csv failist teemale vastavad küsimused
    with open('test.csv', newline="") as küsimused:
        lugeja = csv.reader(küsimused, delimiter=" ", quotechar="|")
        for rida in lugeja:
            if " ".join(rida)[0].isnumeric() and int(" ".join(rida)[0]) == id: # Kontrollib et ei ole esimene rida ja kas on tahetud id
                print((" ".join(rida)).split(";")[1])

def index(request):
    get_questions(2)
    template = loader.get_template('app/base.html')
    return HttpResponse(template.render())
