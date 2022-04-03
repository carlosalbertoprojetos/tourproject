from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Validity, Season, Period


#===============================================================================
# VIGÊNCIA


class ValidityListView(LoginRequiredMixin, ListView):
    model = Validity
    template_name = 'season/validity_list.html'

validity_list = ValidityListView.as_view()


class ValidityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Validity
    fields = '__all__'
    template_name = 'season/validity_create.html'
    success_message = 'Vigência cadastrada com sucesso!!!'
    success_url = _('season:validity_list')
    
validity_create = ValidityCreateView.as_view()


class ValidityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Validity
    fields = '__all__'
    template_name = 'season/validity_update.html'
    success_message = 'Vigência alterada com sucesso!!!'
    success_url = _('season:validity_list')

validity_update = ValidityUpdateView.as_view()


class ValidityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Validity
    template_name = 'season/validity_delete.html'
    success_message = 'Vigência deletada com sucesso!'
    success_url = _('season:validity_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(ValidityDeleteView, self).delete(request, *args, **kwargs)

validity_delete = ValidityDeleteView.as_view()


#===============================================================================
# TEMPORADA


class SeasontListView(ListView):
    model = Season
    template_name = 'season/seasons_list.html'

seasons_list = SeasontListView.as_view()


class SeasonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    
    model = Season
    fields = '__all__'
    template_name = 'season/season_create.html'
    success_message = 'Temporada cadastrada com sucesso!!!'
    success_url = _('season:seasons_list')

season_create = SeasonCreateView.as_view()


class SeasonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    
    model = Season
    fields = '__all__'
    template_name = 'season/season_update.html'
    success_url = _('season:seasons_list')
    success_message = 'Temporada alterada com sucesso!!!'

season_update = SeasonUpdateView.as_view()


class SeasonDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Season
    template_name = 'season/season_delete.html'
    success_message = 'Temporada deletada com sucesso!'
    success_url = _('season:seasons_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(SeasonDeleteView, self).delete(request, *args, **kwargs)

season_delete = SeasonDeleteView.as_view()


#===============================================================================
# PERÍODO


class PeriodListView(LoginRequiredMixin, ListView):
    model = Period
    template_name = 'season/period_list.html'

period_list = PeriodListView.as_view()


class PeriodCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Period
    fields = '__all__'
    template_name = 'season/period_create.html'
    success_message = 'Período cadastrado com sucesso!!!'
    success_url = _('season:period_list')

period_create = PeriodCreateView.as_view()


class PeriodUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Period
    fields = '__all__'
    template_name = 'season/period_update.html'
    success_message = 'Período alterado com sucesso!!!'
    success_url = _('season:period_list')

period_update = PeriodUpdateView.as_view()


class PeriodDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Period
    template_name = 'season/period_delete.html'
    success_message = 'Período deletado com sucesso!'
    success_url = _('season:period_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(PeriodDeleteView, self).delete(request, *args, **kwargs)

period_delete = PeriodDeleteView.as_view()