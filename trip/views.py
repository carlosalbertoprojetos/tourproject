from urllib import request
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from .forms import TripCategoryForm, TripForm
from .models import TripCategory, Trip, TripSeasonPrices



# ------------------------- CATEGORIA DE PASSEIO  -------------------------

class TripCategoryListCreateView(LoginRequiredMixin, ListView):
    model = TripCategory
    template_name = 'trip/trip_category_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TripCategoryListCreateView, self).get_context_data(**kwargs)
        context['form_cat'] = TripCategoryForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form_cat = TripCategoryForm(request.POST or None)

        if form_cat.is_valid():
            form_cat.save(commit=True)
            messages.success(request, 'Categoria criada com sucesso!!!')
            return redirect('trip:trip_category_list_create')
        else:
            return render(request, 'trip/trip_category_list_create.html', {'object':'object','form_cat': form_cat})

trip_list_category_create = TripCategoryListCreateView.as_view()


class TripCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TripCategory
    form_class = TripCategoryForm
    template_name = 'trip/trip_category_update.html'
    success_message = 'Categoria atualizada com sucesso!!!'
    success_url = _('trip:trip_category_list_create')

trip_category_update = TripCategoryUpdateView.as_view()


class TripCategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TripCategory
    template_name = 'trip/trip_category_delete.html'
    success_message = 'Categoria deletada com sucesso!!!'
    success_url = _('trip:trip_category_list_create')

    def delete(self, request, *args, **kwargs):
        return super(TripCategoryDeleteView, self).delete(request, *args, **kwargs)

trip_category_delete = TripCategoryDeleteView.as_view()


# ------------------------- PASSEIO  -------------------------

class TripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'trip/trip_list.html'

trip_list = TripListView.as_view()


class TripCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_create.html'
    success_message = 'Passeio cadastrado com sucesso!!!'
    success_url = _('trip:trip_list')

trip_create = TripCreateView.as_view()


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


# ------------------------- PREÇO  -------------------------

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