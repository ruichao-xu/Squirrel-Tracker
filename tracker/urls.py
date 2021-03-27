from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
     path('', views.index),
     path('map', views.map),
     path('sightings', views.sightings),
     path('sightings/stats', views.stat),
]
