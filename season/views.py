from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Validity, OptionsPrices, PricesSeasonsDestinies
from .forms import PricesCreateForm

class SeasontListView(ListView):
    model = Validity
    template_name = 'season/seasons_list.html'

seasons_list = SeasontListView.as_view()

class SeasonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    
    model = Validity
    fields = '__all__'
    template_name = 'season/season_create.html'
    success_message = 'Temporada cadastrada com sucesso!!!'
    success_url = _('season:seasons_list')

season_create = SeasonCreateView.as_view()

class SeasonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    
    model = Validity
    fields = '__all__'
    template_name = 'season/season_update.html'
    success_url = _('season:seasons_list')
    success_message = 'Temporada alterada com sucesso!!!'

season_update = SeasonUpdateView.as_view()

class SeasonDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Validity
    template_name = 'season/season_delete.html'
    success_message = 'Temporada deletada com sucesso!'
    success_url = _('season:seasons_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(SeasonDeleteView, self).delete(request, *args, **kwargs)

season_delete = SeasonDeleteView.as_view()




# ------------------------- OPTIONS PRICES -------------------------

class OptionPriceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = OptionsPrices
    fields = '__all__'
    template_name = 'season/options_prices_create.html'
    success_message = 'Opção cadastrada com sucesso!!!'
    success_url = _('season:seasons_list')

options_prices_create = OptionPriceCreateView.as_view()

class OptionPricesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = OptionsPrices
    fields = '__all__'
    template_name = 'season/options_prices_update.html'
    success_message = 'Opção alterada com sucesso!!!'
    success_url = _('season:seasons_list')

options_prices_update = OptionPricesUpdateView.as_view()

class OptionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = OptionsPrices
    template_name = 'season/options_prices_delete.html'
    success_message = 'Opção deletada com sucesso!'
    success_url = _('season:seasons_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(OptionDeleteView, self).delete(request, *args, **kwargs)

prices_season_delete = OptionDeleteView.as_view()



# ------------------------- PREÇOS POR DESTINOS/TEMPORADAS -------------------------

class PricesListView(LoginRequiredMixin, ListView):
    model = PricesSeasonsDestinies
    template_name = 'season/prices_seasons_list.html'

    def get_context_data(self, **kwargs):
        context = super(PricesListView, self).get_context_data(**kwargs)
        context['order'] = PricesCreateForm(self.request.POST or None)
        return context


prices_season_list = PricesListView.as_view()


class PricesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PricesSeasonsDestinies
    fields = '__all__'
    template_name = 'season/prices_season_create.html'
    success_message = 'Preço cadastrado com sucesso!!!'
    success_url = _('season:prices_season_list')    
    
prices_season_create = PricesCreateView.as_view()

class PricesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PricesSeasonsDestinies
    fields = '__all__'
    template_name = 'season/prices_season_update.html'
    success_message = 'Valor alterado com sucesso!!!'
    success_url = _('season:prices_season_list')

prices_season_update = PricesUpdateView.as_view()

class PricesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PricesSeasonsDestinies
    template_name = 'season/prices_season_delete.html'
    success_message = 'Valor deletado com sucesso!'
    success_url = _('season:prices_season_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(PricesDeleteView, self).delete(request, *args, **kwargs)

prices_season_delete = PricesDeleteView.as_view()