from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm

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
    sightings = Sighting.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, template_name, context)

def sighting_add(request, template_name='tracker/sighting_form.html'):
    form = SightingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})

def sighting_update(request, pk, template_name='tracker/sighting_form.html'):
    sighting = get_object_or_404(Sighting, pk=pk)
    form = SightingForm(request.POST or None, instance=sighting)
    if form.is_valid():
        form.save()
        return redirect('sighting_list')
    return render(request, template_name, {'form':form})

def sighting_delete(request, pk, template_name='tracker/sighting_confirm_delete.html'):
    sighting = get_object_or_404(Sighting, pk=pk)
    if request.method=='POST':
        sighting.delete()
        return redirect('sighting_list')
    return render(request, template_name, {'object':sighting})

