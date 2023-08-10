from django.shortcuts import render
from django.http import HttpResponse
from .models import Dunk, Pass
from django.contrib.postgres.search import SearchVector, SearchQuery
from .trainmaker import make_a_train
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db import connection


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


# def searchPageView(request): 
#     try: 
#         name = request.GET['name']
        
#         db_dunks = Dunk.objects.filter(name=name) 
        
#     except: 
#         db_dunks = Dunk.objects.all()
    
#     try: 
#         name = request.GET['name']
        
#         db_passes = Pass.objects.filter(name=name) 
        
#     except: 
#         db_passes = Pass.objects.all()
    
    

#     context = {
#         'dunks' : db_dunks,
#         'passes' : db_passes
#     }

#     return render(request, "dunktionaryApp/search.html", context)
# ^^works



# def searchPageView(request):

#     name = request.GET['name']

#     db_dunks = Dunk.objects.filter(
#         Q(name__search=name) | Q(name__icontains=name)
#     )

#     db_passes = Pass.objects.filter(
#         Q(name__search=name) | Q(name__icontains=name)
#     )

#     context = {
#         'dunks': db_dunks,
#         'passes': db_passes,
#     }

#     return render(request, "dunktionaryApp/search.html", context)

# def searchPageView(request): 
#     try:
#         query = request.GET.get('name')
#         if query:
#             db_dunks = Dunk.objects.filter(name__search=query)
#             db_passes = Pass.objects.filter(name__search=query)
#         else:
#             db_dunks = Dunk.objects.none()
#             db_passes = Pass.objects.none()

#     except Exception as e:
#         db_dunks = Dunk.objects.none()
#         db_passes = Pass.objects.none()

#     context = {
#         'dunks': db_dunks,
#         'passes': db_passes,
#     }

#     return render(request, "dunktionaryApp/search.html", context)

def searchPageView(request):
    name = request.GET.get('name', '') 

    if name:
        db_dunks = Dunk.objects.filter(name__search=name)
        db_passes = Pass.objects.filter(name__search=name)
    else:
        db_dunks = Dunk.objects.none()  
        db_passes = Pass.objects.none()  

    context = {
        'dunks': db_dunks,
        'passes': db_passes
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