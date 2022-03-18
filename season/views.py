from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Season


class SeasontListView(ListView):
    model = Season
    template_name = 'season/seasons_list.html'

seasons_list = SeasontListView.as_view()


class SeasonCreateView(SuccessMessageMixin, CreateView):
    
    model = Season
    fields = '__all__'
    template_name = 'season/season_create.html'
    success_message = 'Temporada cadastrada com sucesso!!!'
    success_url = _('season:seasons_list')
    
    

season_create = SeasonCreateView.as_view()


class SeasonUpdateView(SuccessMessageMixin, UpdateView):
    
    model = Season
    fields = '__all__'
    template_name = 'season/season_update.html'
    success_message = 'Dados alterados com sucesso!!!'
    success_url = _('season:seasons_list')

season_update = SeasonUpdateView.as_view()


class SeasonDeleteView(DeleteView):
    model = Season
    template_name = 'season/season_delete.html'
    success_message = 'Temporada deletada com sucesso!'
    success_url = _('season:seasons_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(SeasonDeleteView, self).delete(request, *args, **kwargs)

season_delete = SeasonDeleteView.as_view()




