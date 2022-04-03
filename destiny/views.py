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

class DestinySeasonListView(LoginRequiredMixin, ListView):

    model = Destiny
    template_name = 'destiny/destinies_season_list.html'


destinies_list_season = DestinyListView.as_view()
