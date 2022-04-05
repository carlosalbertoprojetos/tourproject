
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import RegisterTransportForm
from .models import Transport ,TransportPrices, Transport_Type, CategoriesPax

#===============================================================================
# TRANSPORTE

class TransortRegisterView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transport
    form_class = RegisterTransportForm
    template_name = 'transport/transport_create.html'
    success_message = 'Transporte cadastrado com sucesso!!!'
    success_url = _('transport:transport_list')

transport_create = TransortRegisterView.as_view()

class TransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transport
    form_class = RegisterTransportForm
    template_name = 'transport/transport_edit.html'
    success_message = 'Dados alterados com sucesso!!!'
    success_url = _('transport:transport_list')

transport_update = TransportUpdateView.as_view()

class TransportListView(ListView):
    model = Transport
    template_name = 'transport/transport_list.html'
    context_object_name = "transports"

transport_list = TransportListView.as_view()

class DeletarTransporteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transport
    template_name = 'transport/transport_delete.html'
    success_url = _('transport:transport_list')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):        
        return super(DeletarTransporteView, self).delete(request, *args, **kwargs)

transport_delete = DeletarTransporteView.as_view()

class CategoryTransportRegisterView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Transport_Type
    fields = '__all__'
    template_name = 'transport/category_transport_register.html'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = _('transport:transport_list')

category_transport_register = CategoryTransportRegisterView.as_view()

#===============================================================================
# CATEGORIA PAX

class CatPaxTransportListView(LoginRequiredMixin, ListView):
    model = CategoriesPax
    template_name = 'transport/catpax_transport_list.html'

catpax_transport_list = CatPaxTransportListView.as_view()

class CatPaxTransportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoriesPax
    fields = '__all__'
    template_name = 'transport/catpax_transport_create.html'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = _('transport/catpax_transport_list')

catpax_transport_create = CatPaxTransportCreateView.as_view()

class CatPaxTransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoriesPax
    fields = '__all__'
    template_name = 'transport/catpax__transport_update.html'
    success_message = 'Categoria atualizada com sucesso!!!'
    success_url = _('transport/catpax_transport_list')

catpax_transport_update = CatPaxTransportUpdateView.as_view()


class CatPaxTransportDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoriesPax
    template_name = 'transport/catpax_transport_delete.html'
    success_message = 'Categoria deletada com sucesso!!!'
    success_url = _('transport/catpax_transport_list')

    def delete(self, request, *args, **kwargs):
        return super(CatPaxTransportDeleteView, self).delete(request, *args, **kwargs)

catpax_transport_delete = CatPaxTransportDeleteView.as_view()

#===============================================================================
# PREÇOS TRANSPORTE

class PriceTransportListView(LoginRequiredMixin, ListView):
    model = TransportPrices
    template_name = 'transport/price_transport_list.html'

price_transport_list = PriceTransportListView.as_view()


class PriceTransportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TransportPrices
    fields = '__all__'
    template_name = 'transport/price_transport_create.html'
    success_message = 'Preço cadastrado com sucesso!!!'
    success_url = _('transport/price_transport_list')

price_transport_create = PriceTransportCreateView.as_view()


class PriceTransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TransportPrices
    fields = '__all__'
    template_name = 'transport/price_transport_update.html'
    success_message = 'Preço atualizado com sucesso!!!'
    success_url = _('transport/price_transport_list')

price_transport_update = PriceTransportUpdateView.as_view()


class PriceTransportDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TransportPrices
    template_name = 'transport/price_transport_delete.html'
    success_message = 'Preço deletado com sucesso!!!'
    success_url = _('transport/price_transport_list')

    def delete(self, request, *args, **kwargs):
        return super(PriceTransportDeleteView, self).delete(request, *args, **kwargs)

price_transport_delete = PriceTransportDeleteView.as_view()