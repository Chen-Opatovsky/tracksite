from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
import random

from .models import Sighting

class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'

def sighting_list(request, template_name='tracker/all.html'):
    sightings = Sighting.objects.all()
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

def sighting_map(request, template_name='tracker/map.html'):
    sightings = Sighting.objects.order_by('?')[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

def sighting_add(request, template_name='tracker/add.html'):
    form = SightingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})

def sighting_update(request, pk, template_name='tracker/sighting_form.html'):
    sighting = get_object_or_404(Sighting, pk=pk)
    form = SightingForm(request.POST or None, instance=sighting)
    if request.method=='POST' and 'update' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('sighting_list')
    if request.method=='POST' and 'delete' in request.POST:
        sighting.delete()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})




