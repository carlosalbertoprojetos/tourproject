from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Season, PeriodSeasons


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
    success_message = 'Temporada alterada com sucesso!!!'
    success_url = _('season:seasons_list')

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




class PeriodSeasonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    
    model = PeriodSeasons
    fields = '__all__'
    template_name = 'season/period_season_create.html'
    success_message = 'Período por temporada cadastrado com sucesso!!!'
    success_url = _('season:period_seasons_list')

period_season_create = PeriodSeasonCreateView.as_view()


class PeriodSeasonSeasontListView(ListView):
    model = PeriodSeasons
    template_name = 'season/period_seasons_list.html'

period_seasons_list = PeriodSeasonSeasontListView.as_view()


class PeriodSeasonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    
    model = PeriodSeasons
    fields = '__all__'
    template_name = 'season/period_season_update.html'
    success_message = 'Período da temporada alterado com sucesso!!!'
    success_url = _('season:period_seasons_list')

period_season_update = PeriodSeasonUpdateView.as_view()


class PeriodSeasonDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PeriodSeasons
    template_name = 'season/period_season_delete.html'
    success_message = 'Temporada deletada com sucesso!'
    success_url = _('season:period_seasons_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(PeriodSeasonDeleteView, self).delete(request, *args, **kwargs)

period_season_delete = PeriodSeasonDeleteView.as_view()