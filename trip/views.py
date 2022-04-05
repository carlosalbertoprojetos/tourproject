from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import TripForm
from .models import Categories, Trip, CategoriesPax, TripSeasonPrices

#===============================================================================
# PASSEIO

class CategoryRegisterView(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Categories
    fields = '__all__'
    template_name = 'trip/category_register.html'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = _('trip:trip_list')

category_register = CategoryRegisterView.as_view()


class TripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'trip/trip_list.html'

trip_list = TripListView.as_view()


class TripRegisterView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_create.html'
    success_message = 'Passeio cadastrado com sucesso!!!'
    success_url = _('trip:trip_list')

trip_create = TripRegisterView.as_view()


class TripUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_update.html'
    success_message = 'Passeio atualizado com sucesso!!!'
    success_url = _('trip:trip_list')

trip_update = TripUpdateView.as_view()


class TripDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Trip
    template_name = 'trip/trip_delete.html'
    success_message = 'Passeio deletado com sucesso!!!'
    success_url = _('trip:trip_list')

    def delete(self, request, *args, **kwargs):
        return super(TripDeleteView, self).delete(request, *args, **kwargs)

trip_delete = TripDeleteView.as_view()

#===============================================================================
# CATEGORIA PAX

class CatPaxListView(LoginRequiredMixin, ListView):
    model = CategoriesPax
    template_name = 'trip/catpax_list.html'

catpax_list = CatPaxListView.as_view()


class CatPaxCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoriesPax
    fields = '__all__'
    template_name = 'trip/catpax_create.html'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = _('trip:catpax_list')

catpax_create = CatPaxCreateView.as_view()


class CatPaxUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoriesPax
    fields = '__all__'
    template_name = 'trip/catpax_update.html'
    success_message = 'Categoria atualizada com sucesso!!!'
    success_url = _('trip:catpax_list')

catpax_update = CatPaxUpdateView.as_view()


class CatPaxDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoriesPax
    template_name = 'trip/catpax_delete.html'
    success_message = 'Categoria deletada com sucesso!!!'
    success_url = _('trip:catpax_list')

    def delete(self, request, *args, **kwargs):
        return super(CatPaxDeleteView, self).delete(request, *args, **kwargs)

catpax_delete = CatPaxDeleteView.as_view()

#===============================================================================
# PREÇOS

class PriceTripListView(LoginRequiredMixin, ListView):
    model = TripSeasonPrices
    template_name = 'trip/price_trip_list.html'

price_trip_list = PriceTripListView.as_view()


class PriceTripCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TripSeasonPrices
    fields = '__all__'
    template_name = 'trip/price_trip_create.html'
    success_message = 'Preço cadastrado com sucesso!!!'
    success_url = _('trip:price_trip_list')

price_trip_create = PriceTripCreateView.as_view()


class PriceTripUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TripSeasonPrices
    fields = '__all__'
    template_name = 'trip/price_trip_update.html'
    success_message = 'Preço atualizado com sucesso!!!'
    success_url = _('trip:price_trip_list')

price_trip_update = PriceTripUpdateView.as_view()


class PriceTripDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TripSeasonPrices
    template_name = 'trip/price_trip_delete.html'
    success_message = 'Preço deletado com sucesso!!!'
    success_url = _('trip:price_trip_list')

    def delete(self, request, *args, **kwargs):
        return super(PriceTripDeleteView, self).delete(request, *args, **kwargs)


price_trip_delete = PriceTripDeleteView.as_view()