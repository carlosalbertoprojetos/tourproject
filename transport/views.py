from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CatPaxTransportForm, TransportTypeForm, TransportForm
from .models import CategoriesPax, Transport, Transport_Type, TransportPrices



#===============================================================================
# TRANSPORTE

class TransportListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Transport
    template_name = 'transport/transport_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TransportListCreateView, self).get_context_data(**kwargs)
        context['form'] = TransportForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TransportForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Transporte criado com sucesso!!!')
            return redirect('transport:transport_list_create')
        else:
            return render(request, 'transport/transport_list_create.html', {'object':'object','form': form})

transport_list_create = TransportListCreateView.as_view()


class TransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transport
    form_class = TransportForm
    template_name = 'transport/transport_edit.html'
    success_message = 'Dados alterados com sucesso!!!'
    success_url = _('transport:transport_list_create')

transport_update = TransportUpdateView.as_view()


class DeletarTransporteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transport
    template_name = 'transport/transport_delete.html'
    success_url = _('transport:transport_list_create')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):        
        return super(DeletarTransporteView, self).delete(request, *args, **kwargs)

transport_delete = DeletarTransporteView.as_view()


#===============================================================================
# CATEGORIA DE TRANSPORTE

class CategoryTransportListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Transport_Type
    template_name = 'transport/category_transport_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryTransportListCreateView, self).get_context_data(**kwargs)
        context['form'] = TransportTypeForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TransportTypeForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria de Transporte criada com sucesso!!!')
            return redirect('transport:category_transport_list_create')
        else:
            return render(request, 'transport/category_transport_list_create.html', {'object':'object','form': form})

category_transport_list_create = CategoryTransportListCreateView.as_view()


class CategoryTransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transport_Type
    form_class = TransportTypeForm
    template_name = 'transport/category_transport_update.html'
    success_message = 'Categoria de Transporte alterada com sucessoo!!!'
    success_url = _('transport:category_transport_list_create')

category_transport_update = CategoryTransportUpdateView.as_view()


class CategoryTransportDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transport_Type
    template_name = 'transport/category_transport_delete.html'
    success_message = 'Categoria de Transporte deletada com sucessoo!!!'
    success_url = _('transport:category_transport_list_create')

    def delete(self, request, *args, **kwargs):
        return super(CatPaxTransportDeleteView, self).delete(request, *args, **kwargs)

category_transport_delete = CategoryTransportDeleteView.as_view()



#===============================================================================
# CATEGORIA PAX

class CatPaxTransportListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = CategoriesPax
    template_name = 'transport/catpax_transport_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CatPaxTransportListCreateView, self).get_context_data(**kwargs)
        context['form'] = CatPaxTransportForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = CatPaxTransportForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria PAX de Transporte criada com sucesso!!!')
            return redirect('transport:catpax_transport_list_create')
        else:
            return render(request, 'transport/catpax_transport_list_create.html', {'object':'object','form': form})

catpax_transport_list_create = CatPaxTransportListCreateView.as_view()


class CatPaxTransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoriesPax
    form_class = TransportForm
    template_name = 'transport/catpax__transport_update.html'
    success_message = 'Categoria PAX de Transporte alterada com sucessoo!!!'
    success_url = _('transport:catpax_transport_list')

catpax_transport_update = CatPaxTransportUpdateView.as_view()


class CatPaxTransportDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoriesPax
    template_name = 'transport/catpax_transport_delete.html'
    success_message = 'Categoria PAX de Transporte deletada com sucessoo!!!'
    success_url = _('transport:catpax_transport_list')

    def delete(self, request, *args, **kwargs):
        return super(CatPaxTransportDeleteView, self).delete(request, *args, **kwargs)

catpax_transport_delete = CatPaxTransportDeleteView.as_view()


#===============================================================================
# PREÇOS DOS TRANSPORTES

class PriceTransportListView(LoginRequiredMixin, ListView):
    model = TransportPrices
    template_name = 'transport/price_transport_list.html'

price_transport_list_create = PriceTransportListView.as_view()


class PriceTransportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TransportPrices
    fields = '__all__'
    template_name = 'transport/price_transport_create.html'
    success_message = 'Preço cadastrado com sucesso!!!'
    success_url = _('transport:price_transport_list')

price_transport_create = PriceTransportCreateView.as_view()


class PriceTransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TransportPrices
    fields = '__all__'
    template_name = 'transport/price_transport_update.html'
    success_message = 'Preço atualizado com sucesso!!!'
    success_url = _('transport:price_transport_list')

price_transport_update = PriceTransportUpdateView.as_view()


class PriceTransportDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TransportPrices
    template_name = 'transport/price_transport_delete.html'
    success_message = 'Preço deletado com sucesso!!!'
    success_url = _('transport:price_transport_list')

    def delete(self, request, *args, **kwargs):
        return super(PriceTransportDeleteView, self).delete(request, *args, **kwargs)

price_transport_delete = PriceTransportDeleteView.as_view()
