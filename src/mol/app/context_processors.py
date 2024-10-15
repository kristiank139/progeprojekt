import os
categories = [x.split('.')[0] for x in os.listdir("data/flashcards")]

def categories_processor(request):            
    return {'categories': categories}