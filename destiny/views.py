from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

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