from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Destiny


class DestinyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Destiny
    fields = '__all__'
    template_name = 'destiny/destiny_create.html'
    success_message = 'Destino criado com sucesso!'
    success_url = _('destiny:destinies_list')


destiny_create = DestinyCreateView.as_view()


class DestinyListView(LoginRequiredMixin, ListView):

    model = Destiny
    template_name = 'destiny/destinies_list.html'


destinies_list = DestinyListView.as_view()


class DestinyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Destiny
    fields = '__all__'
    template_name = 'destiny/destiny_update.html'
    success_message = 'Destino atualizado com sucesso!!!'
    success_url = _('destiny:destinies_list')


destiny_update = DestinyUpdateView.as_view()


class DestinyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Destiny
    template_name = 'destiny/destiny_delete.html'
    success_url = _('destiny:destinies_list')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DestinyDeleteView, self).delete(request, *args, **kwargs)


destiny_delete = DestinyDeleteView.as_view()

<<<<<<< HEAD

# class DestinyPeriodSeasonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    
#     model = DestinyPeriodSeasons
#     fields = '__all__'
#     template_name = 'destiny/destiny_period_season_create.html'
#     success_message = 'Período por temporada cadastrado com sucesso!!!'
#     success_url = _('destiny:destiny_period_seasons_list')

# destiny_period_season_create = DestinyPeriodSeasonCreateView.as_view()


# class DestinyPeriodSeasonSeasontListView(ListView):
    
#     model = DestinyPeriodSeasons
#     template_name = 'destiny/destiny_period_seasons_list.html'

# destiny_period_seasons_list = DestinyPeriodSeasonSeasontListView.as_view()


# class DestinyPeriodSeasonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    
#     model = DestinyPeriodSeasons
#     fields = '__all__'
#     template_name = 'destiny/destiny_period_season_update.html'
#     success_message = 'Período da temporada alterado com sucesso!!!'
#     success_url = _('destiny:destiny_period_seasons_list')

# destiny_period_season_update = DestinyPeriodSeasonUpdateView.as_view()


# class DestinyPeriodSeasonDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    
#     model = DestinyPeriodSeasons
#     template_name = 'destiny/destiny_period_season_delete.html'
#     success_message = 'Temporada deletada com sucesso!'
#     success_url = _('destiny:destiny_period_seasons_list')
=======
class DestinySeasonListView(LoginRequiredMixin, ListView):

    model = Destiny
    template_name = 'destiny/destinies_season_list.html'
>>>>>>> novo_transport

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request,self.success_message)
#         return super(DestinyPeriodSeasonDeleteView, self).delete(request, *args, **kwargs)

# destiny_period_season_delete = DestinyPeriodSeasonDeleteView.as_view()