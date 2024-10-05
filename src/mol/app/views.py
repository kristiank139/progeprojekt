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
            küsimused[i] = rida[2]
            i += 1

        return küsimused

def flashcards(request, aine):
    küsimused = get_questions(aine)
    return render(request, 'app/flashcard.html', {"küsimused": küsimused})

def riigieksam(request):
    return render(request, 'app/riigieksam.html')

def index(request):
    return render(request, 'app/home.html')
