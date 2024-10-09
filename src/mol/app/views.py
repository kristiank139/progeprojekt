from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader
import csv
    
def get_cards(aine): # Hakkab lugema csv failist teemale vastavad küsimused
    with open(f'data/{aine}.csv', newline="") as f:
        lugeja = csv.reader(f, delimiter=";", quotechar="|")
        card = []
        i = 0
        for rida in lugeja:
            card.append({"description": rida[1], "latex": rida[2]})
            print(card[i])
            i += 1
        return card

def flashcards(request, aine):
    küsimused = get_cards(aine)
    return render(request, 'app/flashcard.html', {"küsimused": küsimused})

def riigieksam(request):
    return render(request, 'app/riigieksam.html')

def index(request):
    return render(request, 'app/home.html')