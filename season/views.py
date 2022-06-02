import pdb
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import SeasonForm, ValidityForm, EventForm
from .models import Season, Validity, Event


#===============================================================================
# EVENTO
def season_event_detail(request, pk):
    #pdb.set_trace()
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
    fields = '__all__'
    template_name = 'season/event_update.html'
    success_message = 'Evento alterado com sucesso!!!'
    #reverse('admin:app_list', kwargs={'app_label': 'auth'})
    success_url = _('season:season_list_create')

event_update = EventUpdateView.as_view()

#===============================================================================
# CALENDÁRIO

def calendar_event_detail(request, pk):
    if pk == None :
        event = get_object_or_404(Season, pk=pk)
    else:
        #pdb.set_trace()
        event = Event.objects.filter(season=pk)
        season = Season.objects.get(pk=pk)
        context = {
            'event':event,
            'season': season,            
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
    model = Season
    template_name = 'season/season_delete.html'
    success_message = 'Temporada deletada com sucesso!'
    success_url = _('season:season_list_create')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(SeasonDeleteView, self).delete(request, *args, **kwargs)

season_delete = SeasonDeleteView.as_view()

