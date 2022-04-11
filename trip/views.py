from urllib import request

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import (TripCategoryForm, TripCategoryPaxForm, TripForm,
                    TripPriceForm)
from .models import Trip, TripCategory, TripCategoryPax, TripPrice



#===============================================================================
# CATEGORIA PAX DE PASSEIO

class TripCategoryPAXListCreateView(LoginRequiredMixin, ListView):
    model = TripCategoryPax
    template_name = 'trip/trip_categorypax_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TripCategoryPAXListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripCategoryPaxForm(self.request.POST or None, self.request.FILES)
        return context

    def post(self, request, *args, **kwargs):
        form = TripCategoryPaxForm(request.POST or None, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria PAX de Passeio criada com sucesso!!!')
            return redirect('trip:trip_categorypax_list_create')
        else:
            return render(request, 'trip/trip_categorypax_list_create.html', {'object':'object','form': form})

trip_categorypax_list_create = TripCategoryPAXListCreateView.as_view()


class TripCategoryPaxUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TripCategoryPax
    form_class = TripCategoryPaxForm
    template_name = 'trip/trip_categorypax_update.html'
    success_message = 'Categoria PAX de Passeio atualizada com sucesso!!!'
    success_url = _('trip:categorypax_list_create')

trip_categorypax_update = TripCategoryPaxUpdateView.as_view()


class TripCategoryPaxDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TripCategoryPax
    template_name = 'trip/trip_categorypax_delete.html'
    success_message = 'Categoria PAX de Passeio deletada com sucesso!!!'
    success_url = _('trip:categorypax_list_create')

    def delete(self, request, *args, **kwargs):
        return super(TripCategoryPaxDeleteView, self).delete(request, *args, **kwargs)

trip_categorypax_delete = TripCategoryPaxDeleteView.as_view()


#===============================================================================
# CATEGORIA DE PASSEIO

class TripCategoryListCreateView(LoginRequiredMixin, ListView):
    model = TripCategory
    template_name = 'trip/trip_category_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TripCategoryListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripCategoryForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TripCategoryForm(request.POST or None)

        if form.is_valid():
            form = form.save()
            messages.success(request, 'Categoria de Passeio criada com sucesso!!!')
            return redirect('trip:trip_category_list_create')
        else:
            return render(request, 'trip/trip_category_list_create.html', {'object':'object','form': form})

trip_category_list_create = TripCategoryListCreateView.as_view()


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


#===============================================================================
# PASSEIO

class TripListCreateView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'trip/trip_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TripListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TripForm(request.POST or None)

        if form.is_valid():
            form = form.save()
            messages.success(request, 'Passeio de Passeio criada com sucesso!!!')
            return redirect('trip:trip_list_create')
        else:
            return render(request, 'trip/trip_list_create.html', {'object':'object','form': form})

trip_list_create = TripListCreateView.as_view()


class TripUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_update.html'
    success_message = 'Passeio atualizado com sucesso!!!'
    success_url = _('trip:trip_list_create')

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
# PREÇOS DOS PASSEIOS

class TripPriceListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = TripPrice
    template_name = 'trip/trip_price_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TripPriceListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripPriceForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TripPriceForm(request.POST or None)

        if form.is_valid():
            form = form.save()
            messages.success(request, 'Valor de Passeio criado com sucesso!!!')
            return redirect('trip:trip_price_list_create')
        else:
            return render(request, 'trip/trip_price_list_create.html', {'object':'object','form': form})

trip_price_list_create = TripPriceListCreateView.as_view()


class TripPriceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TripPrice
    form_class = TripPriceForm
    template_name = 'trip/trip_price_update.html'
    success_message = 'Valor de Passeio atualizado com sucesso!!!'
    success_url = _('trip:trip_price_list_create')

trip_price_update = TripPriceUpdateView.as_view()


class TripPriceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TripPrice
    template_name = 'trip/trip_price_delete.html'
    success_message = 'Valor de Passeio deletado com sucesso!!!'
    success_url = _('trip:trip_price_list_create')

    def delete(self, request, *args, **kwargs):
        return super(TripPriceDeleteView, self).delete(request, *args, **kwargs)

trip_price_delete = TripPriceDeleteView.as_view()
