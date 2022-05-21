import pdb
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import SeasonForm, ValidityForm, EventForm
from .models import Season, Validity, Event


#===============================================================================
# CALENDÁRIO

class CalendarEventView(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model = Event
    template_name = 'season/calendar_event.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarEventView, self).get_context_data(**kwargs)
        context['form'] = EventForm(self.request.POST or None)
        return context

    def post(self,request, *args, **kwargs):            
            form = EventForm(request.POST or None)
            #pdb.set_trace()
            if form.is_valid():
                form.save()
                messages.success(request, 'Evento salvo com sucesso!!!')
                return redirect('season:calendar_event')
            else:
                messages.success(request, 'Erro ao salvar evento!!!')
                return render(request, 'season/calendar_event.html', {'object':'object','form': form})
calendar_event = CalendarEventView.as_view()

class CalendarListView(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model = Event
    template_name = 'season/calendar_list.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarListView, self).get_context_data(**kwargs)
        context['form'] = EventForm(self.request.POST or None)
        return context
    
calendar_list = CalendarListView.as_view()

class CalendarCreateView(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model = Event
    template_name = 'season/calendar_create.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarCreateView, self).get_context_data(**kwargs)
        context['form'] = EventForm(self.request.POST or None)
        return context

    def post(self,request, *args, **kwargs):            
            form = EventForm(request.POST or None)
            #pdb.set_trace()
            if form.is_valid():
                form.save()
                messages.success(request, 'Evento salvo com sucesso!!!')
                return redirect('season:calendar_create')
            else:
                messages.success(request, 'Erro ao salvar evento!!!')
                return render(request, 'season/calendar_create.html', {'object':'object','form': form})

calendar_create = CalendarCreateView.as_view()

class CalendarDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    template_name = 'season/calendar_delete.html'
    success_message = 'Evento deletada com sucesso!'
    success_url = _('season:calendar_event')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(CalendarDeleteView, self).delete(request, *args, **kwargs)

calendar_delete = CalendarDeleteView.as_view()
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

