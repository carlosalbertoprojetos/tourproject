from fileinput import close
import pdb
from datetime import datetime, timedelta, date
from django.core.exceptions import ValidationError
import json
import sys
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SeasonForm, ValidityForm, EventForm

from .models import Season, Validity, Event 


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'season/event_create.html'    
    
    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST or None)        
        season_pk = self.kwargs.get('season_id')        
        event = Event.objects.filter(season=season_pk)               
        season = Season.objects.get(id=season_pk)   
        
        if form.is_valid():
            form = form.save(commit=False)
            form.season_id = season_pk
            form.save()
            messages.success(request, 'Evento criada com sucesso!!!')
            return HttpResponseRedirect("/season/"+str(season_pk)+"/event/detail")
        else:
            return render(request, 'season/event_create.html', {'object':'object','form': form})

event_create_view = EventCreateView.as_view()


def event_list(request, pk):
    context = {}
    form = EventForm(request.POST or None)
    season = Season.objects.get(pk=pk)
    event = Event.objects.filter(season__id=pk)    
    context = {
        'event':event,        
        'season': season,
        'form': form,            
    }
             
    if form.is_valid():
        form.save()
        messages.success(request, 'Evento criado com sucesso!!!')    
        return render(request, 'season/event_list.html', context)
    else:         
         return render(request, 'season/event_list.html', context)  


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):    
  
    model = Event
    form_class = EventForm 
    template_name = 'season/event_update.html'
    success_message = 'Evento alterado com sucesso!!!'   

    def post(self, request, **kwargs):        
        season_pk = self.kwargs.get('season_id')
        pk = self.kwargs.get('pk')        
        
        obj = get_object_or_404(Event, pk=pk)
        form = EventForm(request.POST or None, instance=obj)       
        if form.is_valid():
            form.save()
            messages.success(self.request,self.success_message)
            return HttpResponseRedirect("/season/"+str(season_pk)+"/event/detail")      

event_update_view = EventUpdateView.as_view()


def event_delete(request, **kwargs):
    
    context ={}
    pk = kwargs.get('pk') 
    
    obj = get_object_or_404(Event, pk = pk) 
 
    if request.method =="POST":
        season_pk = kwargs.get('season_id')
        obj.delete()
        messages.success(request, 'Evento deletado com sucesso!!!')
        return HttpResponseRedirect("/season/"+str(season_pk)+"/event/detail")
 
    return render(request, "season/event_delete.html", context)


def calendar_event_detail(request, pk):
    list_dates= []        
    year = {}
    events = []
    list_dates_str = ""       
       
    if pk == None :
        event = get_object_or_404(Event, pk=pk)
    else:                    
        event = Event.objects.filter(season=pk)               
        season = Season.objects.get(pk=pk)
        for e in event:
            events.append(e.name_event)            
        
        for e in Event.objects.filter(season=pk):               
            date_init_list = e.date_init #.strftime("%-d/%-m/%Y")           
            date_fin_list = e.date_fin #.strftime("%-d/%-m/%Y")                            
            delta = date_fin_list - date_init_list           
            if date_init_list > date_fin_list:
                messages.success(request, "Erro ao mostrar calendário de eventos. Verifique as datas cadastradas!!!")
           
            else:
                for i in range(delta.days + 1):
                    day = date_init_list + timedelta(days=i)
                    list_dates.append(day)
           
                list_dates_str = [datetime.strftime(dt, format="%-d/%-m/%Y") for dt in list_dates]               
                year = season.validity.year 

        #locahost/heroku
        sys.stdout = open('basics/static/js/vet_dates.js','w')
        vet_dates = json.dumps(list_dates_str)           
        vet_events = json.dumps(events)

        print("var vet_dates ='{}'".format(vet_dates))
        print("var year = '{}'".format(year))
        print("var events = '{}'".format(vet_events))
        
        context = {                        
            'event': event,
            'season': season,
            'range': range(0,13),
            }    
        sys.stdout = close()
        return render(request, 'season/calendar_list.html', context)


class ValidityListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Validity
    template_name = 'season/validity_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(ValidityListCreateView, self).get_context_data(**kwargs)
        context['form'] = ValidityForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = ValidityForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Vigência criada com sucesso!!!')
            return redirect('season:validity_list_create')
        else:
            return render(request, 'season/validity_list_create.html', {'object':'object','form': form})

validity_list_create = ValidityListCreateView.as_view()


class ValidityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Validity
    form_class = ValidityForm
    template_name = 'season/validity_update.html'
    success_message = 'Vigência alterada com sucesso!!!'
    success_url = _('season:validity_list_create')

validity_update = ValidityUpdateView.as_view()


class ValidityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    try:
        model = Validity    
        template_name = 'season/validity_delete.html'
        success_message = 'Vigência deletada com sucesso!'
        success_url = _('season:validity_list_create')        

    except IntegrityError:
         success_message = 'Erro ao deletar Vigência!!!'
         success_url = _('season:validity_list_create')    

validity_delete = ValidityDeleteView.as_view()


class SeasonListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Season
    template_name = 'season/season_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(SeasonListCreateView, self).get_context_data(**kwargs)
        context['form'] = SeasonForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = SeasonForm(request.POST or None)
        if form.is_valid():            
            form.save()
            messages.success(request, 'Temporada criada com sucesso!!!')
            return redirect('season:season_list_create')
        else:
            return render(request, 'season/season_list_create.html', {'object':'object','form': form})

season_list_create = SeasonListCreateView.as_view()


class SeasonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    
    model = Season
    form_class = SeasonForm
    template_name = 'season/season_update.html'
    success_url = _('season:season_list_create')
    success_message = 'Temporada alterada com sucesso!!!'

season_update = SeasonUpdateView.as_view()


class SeasonDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):    
    try:
        model = Season        
        template_name = 'season/season_delete.html'
        success_message = 'Temporada deletada com sucesso!!!'
        success_url = _('season:season_list_create')      

    except IntegrityError:
         success_message = 'Erro ao deletar temporada!!!'
         success_url = _('season:season_list_create')

season_delete = SeasonDeleteView.as_view()

