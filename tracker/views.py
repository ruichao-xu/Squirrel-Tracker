from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import AddSightingsForm
from .forms import UpdateForm

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
    form = UpdateForm(instance = squirrel)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/sightings')

    context = {
            'squirrel':  squirrel,
            'form': form,
            }

    return render(request, 'tracker/detail.html',context)

def add(request):
    if request.method == 'POST':
        form = AddSightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
        else:
            return JsonResponse({'errors': form.errors}, status = 400)
    return render(request, 'tracker/add.html', {})
