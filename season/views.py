import pdb
from django import views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import PeriodForm, SeasonForm, ValidityForm, EventForm, CommentForm
from .models import Period, Season, Validity, Event



#template_name = 'season/calendar_view.html'

def calendar_event(request):
    form = CommentForm()
    return render(request, "season/calendar_event.html", {'form':form}) 

def mode_calendar(request):    
    return render(request, "season/mode_calendar.html")     

#===============================================================================
# CALENDÁRIO
class CalendarListCreateView(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model = Event
    template_name = 'season/calendar_list_create.html'

    def get_context_data(self, **kwargs):
        context = super(CalendarListCreateView, self).get_context_data(**kwargs)
        context['form'] = EventForm(self.request.POST or None)
        return context

    def post(self,request, *args, **kwargs):            
            form = EventForm(request.POST or None)
            #pdb.set_trace()
            if form.is_valid():
                form.save()
                messages.success(request, 'Evento salvo com sucesso!!!')
                return redirect('season:calendar_list_create')
            else:
                messages.success(request, 'Erro ao salvar evento!!!')
                return render(request, 'season/calendar_list_create.html', {'object':'object','form': form})
                

calendar_list_create = CalendarListCreateView.as_view()

class CalendarDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    template_name = 'season/calendar_delete.html'
    success_message = 'Evento deletada com sucesso!'
    success_url = _('season:calendar_list_create')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(CalendarDeleteView, self).delete(request, *args, **kwargs)

calendar_delete = CalendarDeleteView.as_view()

class CalendarCreateView(LoginRequiredMixin, SuccessMessageMixin,ListView):
    model = Event
    template_name = 'season/calendar_new.html'

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
                return redirect('season:calendar_list_create')
            else:
                messages.success(request, 'Erro ao salvar evento!!!')
                return render(request, 'season/calendar_list_view.html', {'object':'object','form': form})
                

calendar_new = CalendarCreateView.as_view()

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


#===============================================================================
# PERÍODO

class PeriodListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Period
    template_name = 'season/period_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(PeriodListCreateView, self).get_context_data(**kwargs)
        context['form'] = PeriodForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = PeriodForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Período criado com sucesso!!!')
            return redirect('season:period_list_create')
        else:
            return render(request, 'season/period_list_create.html', {'object':'object','form': form})

period_list_create = PeriodListCreateView.as_view()


class PeriodUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Period
    fields = '__all__'
    template_name = 'season/period_update.html'
    success_message = 'Período alterado com sucesso!!!'
    success_url = _('season:period_list_create')

period_update = PeriodUpdateView.as_view()


class PeriodDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Period
    template_name = 'season/period_delete.html'
    success_message = 'Período deletado com sucesso!!!'
    success_url = _('season:period_list_create')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(PeriodDeleteView, self).delete(request, *args, **kwargs)

period_delete = PeriodDeleteView.as_view()