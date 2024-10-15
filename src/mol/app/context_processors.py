import os
from django.conf import settings  # Import settings

flashcards_dir = os.path.join(settings.BASE_DIR, 'data', 'flashcards')
categories = [x.split('.')[0] for x in os.listdir(flashcards_dir)]

def categories_processor(request):
    return {'categories': categories}