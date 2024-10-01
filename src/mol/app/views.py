from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader
import csv

def get_questions(id): # Hakkab lugema csv failist teemale vastavad küsimused
    with open('test.csv', newline="") as küsimused:
        lugeja = csv.reader(küsimused, delimiter=" ", quotechar="|")
        küsimused = []
        for rida in lugeja:
            if " ".join(rida)[0].isnumeric() and int(" ".join(rida)[0]) == id: # Kontrollib et ei ole esimene rida ja kas on tahetud id
                küsimused.append((" ".join(rida)).split(";")[1])

        return küsimused

def index(request, id):
    küsimused = get_questions(id)
    return render(request, 'app/base.html',{"küsimused": küsimused})
