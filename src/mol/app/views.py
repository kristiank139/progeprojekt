from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader
import csv

def get_questions(aine): # Hakkab lugema csv failist teemale vastavad küsimused
    with open(f'data/{aine}.csv', newline="") as küsimused:
        lugeja = csv.reader(küsimused, delimiter=";", quotechar="|")
        küsimused = {}
        i = 0
        for rida in lugeja:
            #if " ".join(rida)[0].isnumeric(): # Kontrollib et ei ole esimene rida
            #    küsimused[i] = (" ".join(rida)).split(";")[1]
            #    i += 1
            küsimused[i] = rida[2]
            i += 1
            print(rida[2])

        print(küsimused)

        return küsimused

def index(request, aine):
    küsimused = get_questions(aine)
    return render(request, 'app/base.html', {"küsimused": küsimused})
