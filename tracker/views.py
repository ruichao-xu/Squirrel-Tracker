from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'tracker/home.html',{})

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'sightings': squirrels,
            }

    return render(request, 'tracker/map.html',context)

def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }

    return render(request, 'tracker/sightings.html',context)

def stat(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
            }

    return render(request, 'tracker/stat.html', context)

def detail(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {
            'squirrel':  squirrel,
            }

    return render(request, 'tracker/detail.html',context)

def add(request):
    return render(request, 'tracker/add.html',{})

