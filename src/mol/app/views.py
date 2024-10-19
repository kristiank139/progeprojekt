from django.shortcuts import render
from . import urls
from django.http import HttpResponse
from django.template import loader
import csv
from django.views.decorators.csrf import ensure_csrf_cookie

# proovib importida API.py faili chatboti jaoks (see fail pole githubis)
try:
    from . import API as f
except ImportError:
    f = None
    print("Ei leidnud API.py mis on vajalik chatboti jaoks")

def get_cards(aine): # Hakkab lugema csv failist teemale vastavad küsimused
    with open(f'data/{aine}.csv', newline="") as f:
        lugeja = csv.reader(f, delimiter=";", quotechar="|")
        card = []
        i = 0
        for rida in lugeja:
            card.append({"description": rida[1], "latex": rida[2]})
            i += 1
        return card

def flashcards(request, aine):
    küsimused = get_cards(aine)
    return render(request, 'app/flashcard.html', {"küsimused": küsimused})

def riigieksam(request):
    return render(request, 'app/riigieksam.html')

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


