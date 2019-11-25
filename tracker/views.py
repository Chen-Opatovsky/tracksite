from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Sighting

def all_sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'tracker/all.html', context)

def add_sighting(request):
    sighting = request.POST
    sighting.save()
    return HttpResponseRedirect('/sightings/')
