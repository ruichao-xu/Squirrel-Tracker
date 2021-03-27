from django.shortcuts import render

from django.http import HttpResponse
from .models import Squirrel

def index(request):
    return render(request, 'tracker/home.html',{})

def map(request):
    squirrels = Squirrel.objects.all()
    context = {
            'sightings': squirrels,
            }

    return render(request, 'tracker/map.html',context)
