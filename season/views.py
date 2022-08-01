import json
import sys
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import SeasonForm, ValidityForm, EventForm
from .models import Season, Validity, Event

import datetime as dt


#===============================================================================
# EVENTO
def season_event_detail(request, pk):
    context = {}
    form = EventForm(request.POST or None)
    event = Event.objects.filter(season=pk)
    season = Season.objects.get(pk=pk)
    context = {
        'event':event,
        'season': season,
        'form': form,
    }
    if form.is_valid():
        form = form.save(commit=False)
        form.season_id = pk
        form.save()
        messages.success(request, 'Evento salvo com sucesso!!!')    
        return render(request, 'season/season_event_list_create.html', context)
    else:
        return render(request, 'season/season_event_list_create.html', context)


class EventDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    template_name = 'season/event_delete.html'
    success_message = 'Evento deletado com sucesso!'
    success_url = _('season:season_list_create')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(EventDeleteView, self).delete(request, *args, **kwargs)

event_delete = EventDeleteView.as_view()


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    # fields = '__all__'
    form_class = EventForm
    template_name = 'season/event_update.html'
    success_message = 'Evento alterado com sucesso!!!'    
    success_url = _('season:season_list_create')

event_update = EventUpdateView.as_view()

#===============================================================================
# CALENDÁRIO

def calendar_event_detail(request, pk):   
    if pk == None :
        event = get_object_or_404(Event, pk=pk)
    else:
        #pdb.set_trace()
        dates = [] # array de datas
        year = {}
        new_dates = {} #dicionario para criar arquivo json     
        event = Event.objects.filter(season=pk)               
        season = Season.objects.get(pk=pk)

        for e in Event.objects.filter(season=pk):
           date_init = e.date_init.strftime("%-d/%-m/%Y")           
           date_fin = e.date_fin.strftime("%-d/%-m/%Y")
           #evento = e.name_event
           year = season.validity.year                        
           dates.extend([date_init,date_fin])          
        
              
        new_dates = {i:dates[i]for i in range(0,len(dates))}
        vet_dates = json.dumps(new_dates)

        #locahost/heroku
        sys.stdout = open('basics/static/js/vet_dates.js','w')       
               
        print("var vet_dates ='{}'".format(vet_dates))
        print("var year = '{}'".format(year))
        
        context = {
            'dates': dates,            
            'event': event,
            'season': season,
            'range': range(0,13),                        
        }    
        
        return render(request, 'season/calendar_list.html', context)

#=====================================================================================================
# VIGÊNCIA

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
    fields = '__all__'
    template_name = 'season/validity_update.html'
    success_message = 'Vigência alterada com sucesso!!!'
    success_url = _('season:validity_list_create')

validity_update = ValidityUpdateView.as_view()

class ValidityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Validity
    template_name = 'season/validity_delete.html'
    success_message = 'Vigência deletada com sucesso!'
    success_url = _('season:validity_list_create')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(ValidityDeleteView, self).delete(request, *args, **kwargs)

validity_delete = ValidityDeleteView.as_view()


#===============================================================================
# TEMPORADA

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

        def delete(self, request, *args, **kwargs):
            messages.success(self.request,self.success_message)
            return super(SeasonDeleteView, self).delete(request, *args, **kwargs)

    except IntegrityError:
         success_message = 'Erro ao deletar temporada!!!'
         success_url = _('season:season_list_create')

season_delete = SeasonDeleteView.as_view()


"""
objetivo:
    Listar todos as atividades(activity) cujos passeios(trip) são relacionados ao destino(destiny) selecionado, dentro do intervalo de tempo informado(event/date_init, date_fin)
    1) Filtrar todas atividades dos passeios relacionados ao destino=1:
    activities = Activity.objects.all().filter(trip__destiny=1)
    2) Filtrar data_init/data_fin, comprar com as datas dos eventos e extrair a season correspondente
"""
from trip.models import Activity, ActivityPrice
import datetime as dt
from django.db.models import Q

# todas as atividades dos passeios relacionadas aos destino = 1
def teste(id_destiny=1):
    start_date = dt.date(2023, 1, 1)
    end_date = dt.date(2023, 1, 9)

    season = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date))).first()

    activities_prices = ActivityPrice.objects.filter(season=season.id)
    activity = Activity.objects.filter(trip__destiny=id_destiny).first()
    activities = Activity.objects.filter(trip_id=activity.id)
    print('Destino: ', activity.trip.destiny, '\n', 'Passeio: ', activity.trip.name)   
    print('\nEventos para', season.season.name, 'em', activity.trip.destiny.name)
    #, end="")
    events = Event.objects.filter(season__name=season.season.name)
    for e in events:
        print(f' {e} de Início:{e.date_init:%d/%m/%Y} a Fim:{e.date_fin:%d/%m/%Y}')

    print('\nAtividades:')
    for a in activities:
        print(' ', a)
        for ap in activities_prices:
            if a == ap.activity:
                print('   ', ap.catpax, ap.price)
    print('\n')
# teste()