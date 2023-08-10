from django.shortcuts import render
from django.http import HttpResponse
from .models import Dunk, Pass
from django.contrib.postgres.search import SearchVector, SearchQuery
from .trainmaker import make_a_train


def indexPageView(request):
    db_dunks = Dunk.objects.all()

    context = {
        "dunk" : db_dunks
    }

    return render(request, 'dunktionaryApp/index.html', context)


def passLibPageView(request):
    db_passes = Pass.objects.all()

    context = {
        "passes" : db_passes
    }

    return render(request, 'dunktionaryApp/passlib.html',context)

def dunkLibPageView(request):
    db_dunks = Dunk.objects.all()

    context = {
        "dunks" : db_dunks
    }

    return render(request, 'dunktionaryApp/dunklib.html', context)

def dunkPageView(request, dunk_altName):
    db_dunks = Dunk.objects.get(altName=dunk_altName)
    db_dunks2 = Dunk.objects.all()
    
    context = {
        "dunk" : db_dunks,
        "dunks" : db_dunks2
    }

    return render(request, "dunktionaryApp/dunk.html", context)

def passPageView(request, pass_altName):
    db_passes = Pass.objects.get(altName=pass_altName)
    db_passes2 = Pass.objects.all()

    context = {
        "pass" : db_passes,
        "passes" : db_passes2,
    }

    return render(request, "dunktionaryApp/pass.html", context)


def searchPageView(request): 
    try: 
        name = request.GET['name']
        
        db_dunks = Dunk.objects.filter(name=name) 
        
    except: 
        db_dunks = Dunk.objects.all()
    
    try: 
        name = request.GET['name']
        
        db_passes = Pass.objects.filter(name=name) 
        
    except: 
        db_passes = Pass.objects.all()
    
    

    context = {
        'dunks' : db_dunks,
        'passes' : db_passes
    }

    return render(request, "dunktionaryApp/search.html", context)
    

def trainPageView(request):
    if request.method == 'POST':
        num_people = int(request.POST.get('num_people', '0'))
        level = int(request.POST.get('level', '0'))
        train = make_a_train(num_people, level)
        context = {'train': train}
        return render(request, 'dunktionaryApp/trainmaker.html', context)
    else:
        return render(request, 'dunktionaryApp/trainmaker.html')    