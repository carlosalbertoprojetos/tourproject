from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import (TripCategoryForm, TripCategoryPaxForm, TripForm,
                    TripOptionsForm, TripPriceForm)
from .models import (Trip, TripCategory, TripCategoryPax, TripOption,
                     TripPrice)

#===============================================================================
# CATEGORIA PAX DE PASSEIO

class TripCategoryPAXListCreateView(LoginRequiredMixin, ListView):
    model = TripCategoryPax
    template_name = 'trip/trip_categorypax_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(TripCategoryPAXListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripCategoryPaxForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TripCategoryPaxForm(request.POST or None)

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
        context['form'] = TripForm(self.request.POST or None, self.request.FILES)
        return context

    def post(self, request, *args, **kwargs):
        form = TripForm(request.POST or None, request.FILES)

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
# OPÇÕES DOS PASSEIO

class TripOptionListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = TripOption
    template_name = 'trip/trip_option_list_create.html'

    # def get_queryset(self, **kwargs):
    #     return TripOption.objects.filter(trip__id=self.kwargs['trip_id'])
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            trip__id=self.kwargs['trip_id']
        )

    def get_context_data(self, **kwargs):
        context = super(TripOptionListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripOptionsForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TripOptionsForm(request.POST or None)

        if form.is_valid():
            form = form.save()
            messages.success(request, 'Opção de Passei criada com sucesso!!!')
            return redirect('trip:trip_option_list_create')
        else:
            return render(request, 'trip/trip_option_list_create.html', {'object':'object','form': form})

trip_option_list_create = TripOptionListCreateView.as_view()


class TripOptionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TripOption
    form_class = TripOptionsForm
    template_name = 'trip/trip_option_update.html'
    success_message = 'Opção de Passeio atualizada com sucesso!!!'
    success_url = _('trip:trip_option_list_create')

trip_option_update = TripOptionUpdateView.as_view()


class TripOptionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TripOption
    template_name = 'trip/trip_option_delete.html'
    success_message = 'Opção de Passeio deletada com sucesso!!!'
    success_url = _('trip:trip_option_list_create')

    def delete(self, request, *args, **kwargs):
        return super(TripOptionDeleteView, self).delete(request, *args, **kwargs)

trip_option_delete = TripOptionDeleteView.as_view()



#===============================================================================
# PREÇOS DOS PASSEIOS

class TripPriceListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = TripPrice
    template_name = 'trip/trip_price_list.html'
 
trip_price_list_create = TripPriceListView.as_view()


# @login_required
def trip_price_update1(request, trip_id):  
    trip_option = TripOption.objects.filter(trip_id=trip_id)
    
    trip_price_formset = modelformset_factory(TripPrice, form=TripPriceForm, extra=0)
    
    for a in trip_option:
        trip = a.trip
        tp = TripPrice.objects.filter(trip_option_id=a)
        
        cadpaxs=[]
        seasons=[]
        activities=[]
        
        for i in tp:
            activities.append(i.trip_option_id)

        activities=list(set(activities))

        for a in activities:
            for i in tp:
                if i.trip_option_id == a:
                    cadpaxs.append(i.cadpax)
                    seasons.append(i.season)

            cadpaxs=list(set(cadpaxs))
            seasons=list(set(seasons))

            if request.method == 'POST':
                formset = trip_price_formset(request.POST, queryset=TripPrice.objects.filter(trip_option_id__id=i.trip_option_id))

                if formset.is_valid():
                    instances = formset.save(commit=False)
                    for instance in instances:
                        instance.trip_option_id = i.trip_option_id
                        instance.save()

                    messages.success(request, 'Preços alterados com sucesso!!!')
                    return redirect('trip:trip_price_update1', trip_id)

            formset = trip_price_formset(queryset=TripPrice.objects.filter(trip_option_id__id=i.trip_option_id))
            
            context = {
                'trip':trip,
                'season':seasons,
                'cadpax':cadpaxs,
                'price': tp,
                'trip_option':trip_option,
                'formset':formset
            }  
            return render(request, 'trip/trip_price_update1.html', context)
    
    
    for a in activities:
        for i in tp:
            if i.trip_option_id == a:
                if request.method == 'POST':
                    formset = trip_price_formset(request.POST, queryset=TripPrice.objects.filter(trip_option_id__id=i.trip_option_id))

                    if formset.is_valid():
                        instances = formset.save(commit=False)
                        for instance in instances:
                            instance.trip_option_id = i.trip_option_id
                            instance.save()

                        messages.success(request, 'Preços alterados com sucesso!!!')
                        return redirect('trip:trip_price_update1', trip_id)

                formset = trip_price_formset(queryset=TripPrice.objects.filter(trip_option_id__id=i.trip_option_id))
                
                context = {
                    'activities':activities,
                    'season':seasons,
                    'cadpax':cadpaxs,
                    'price': tp,
                    'trip_option':trip_option,
                    'formset':formset
                }  
                return render(request, 'trip/trip_price_update1.html', context)


def trip_price_update(request, trip_option_id):
    trip_option = TripOption.objects.filter(id=trip_option_id)
    
    tp = TripPrice.objects.filter(trip_option_id=trip_option_id)
    trip_price_formset = modelformset_factory(TripPrice, form=TripPriceForm, extra=0)

    cadpaxs=[]
    seasons=[]
    activities=[]
    for i in tp:
        cadpaxs.append(i.cadpax)
        seasons.append(i.season)
        if not i.trip_option_id in activities:
            activities.append(i.trip_option_id)

    activities=list((activities))
    cadpaxs=list(set(cadpaxs))
    seasons=list(set(seasons))

    # for a in trip_option:
    #     top = TripPrice.objects.filter(trip_option_id=a.id)

    for i in tp:
        for a in seasons:
            if request.method == 'POST':
                formset = trip_price_formset(request.POST, queryset=TripPrice.objects.filter(trip_option_id=trip_option_id))
                if formset.is_valid():
                    instances = formset.save(commit=False)
                    for instance in instances:
                        instance.trip_option_id = trip_option_id
                        instance.save()

                    messages.success(request, 'Preços alterados com sucesso!!!')
                    return redirect('trip:tripop_price_update', trip_option_id)

            formset = trip_price_formset(queryset=TripPrice.objects.filter(
                trip_option_id=trip_option_id
                )
            )

            context = {
                'season':seasons,
                'cadpax':cadpaxs,
                'trip_option':trip_option,
                'formset':formset
            }  
            return render(request, 'trip/trip_price_update.html', context)


class TripPriceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TripPrice
    template_name = 'trip/trip_price_delete.html'
    success_message = 'Valor de Passeio deletado com sucesso!!!'
    success_url = _('trip:trip_price_list')

    def delete(self, request, *args, **kwargs):
        return super(TripPriceDeleteView, self).delete(request, *args, **kwargs)

trip_price_delete = TripPriceDeleteView.as_view()
