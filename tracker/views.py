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

def sighting_stats(request, template_name='tracker/stats.html'):
    all_count = Sighting.objects.all().count()

    latest_date = Sighting.objects.raw('SELECT squirrel_id FROM tracker_sighting ORDER BY date DESC')[0]

    morning_shifts_adult = Sighting.objects.filter(shift='AM', age='Adult').count()
    morning_shifts_juvenile = Sighting.objects.filter(shift='AM', age='Juvenile').count()
    if morning_shifts_adult > morning_shifts_juvenile:
        age_morning_shift = 'Adults'
    else:
        age_morning_shift = 'Juveniles'

    black_fur = int(100*round(Sighting.objects.filter(fur_color='Black').count()/all_count,2))
    gray_fur = int(100*round(Sighting.objects.filter(fur_color='Gray').count()/all_count,2))
    cinnamon_fur = int(100*round(Sighting.objects.filter(fur_color='Cinnamon').count()/all_count,2))
    no_fur_color = int(100*round(Sighting.objects.filter(fur_color='').count()/all_count,2))
    activities = dict()
    activities['running'] = Sighting.objects.filter(running=True).count()
    activities['chasing'] = Sighting.objects.filter(chasing=True).count()
    activities['climbing'] = Sighting.objects.filter(climbing=True).count()
    activities['eating'] = Sighting.objects.filter(eating=True).count()
    activities['foraging'] = Sighting.objects.filter(foraging=True).count()
    
    most_common_activity = ''
    activity_count = 0
    for activity in activities:
        if activities[activity] > activity_count:
            most_common_activity = activity
            activity_count = activities[activity]
        else:
            pass

    context = {
            'all_count' : all_count,
            'latest_date' : latest_date,
            'age_morning_shift' : age_morning_shift,
            'black_fur' : black_fur,
            'gray_fur' : gray_fur,
            'cinnamon_fur' : cinnamon_fur,
            'no_fur_color' : no_fur_color,
            'most_common_activity' : most_common_activity,
            'activity_count' : activity_count,
    }
    return render(request, template_name, context)


