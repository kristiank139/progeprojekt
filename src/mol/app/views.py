from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader
import csv
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings  # Import settings
import os
import random as r

data_dir = os.path.join(settings.BASE_DIR, 'data')

# proovib importida API.py faili chatboti jaoks (see fail pole githubis)
try:
    from . import API as f
except ImportError:
    f = None
    print("Ei leidnud API.py mis on vajalik chatboti jaoks")


def get_cards(aine): # Hakkab lugema csv failist teemale vastavad küsimused
    file_path = os.path.join(data_dir, 'flashcards', f'{aine}.csv')
    with open(file_path, encoding="utf-8") as f:
        lugeja = csv.reader(f, delimiter=";", quotechar='"')
        cards = []
        i = 0
        for rida in lugeja:
            cards.append({"description": rida[1], "latex": rida[2]})
            i += 1
        r.shuffle(cards) # Shufflib kaardid ära, siis tulevad valemid suvaliselt
        return cards
    
def get_exercises():
    file_path = os.path.join(data_dir, 'riigieksam.csv')
    with open(file_path, newline="" , encoding="utf-8") as f:
        lugeja = csv.reader(f, delimiter=",", quotechar='"')
        exercises = []
        i = 0
        for rida in lugeja:
            print(rida)
            exercises.append({"name": rida[0], "text": rida[1], "figure": rida[2], "solutionImage": rida[3]})
            i += 1
        return exercises

def flashcards(request, aine):
    küsimused = get_cards(aine)
    return render(request, 'app/flashcard.html', {"küsimused": küsimused})

def riigieksam(request):
    exercises = get_exercises()
    return render(request, 'app/riigieksam.html' , {"exercises": exercises})


def index(request):
    return render(request, 'app/home.html')

@ensure_csrf_cookie
def chatRobot(request):

    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        # Kui API.py faili ei leita, siis tagastab API ei ole saadaval hetkel
        if f is None:
            return HttpResponse('Chatbot API ei ole saadaval hetkel')
        aiResponse = f.my_function(prompt)
        return HttpResponse(aiResponse)
    return HttpResponse('Hello World!')


