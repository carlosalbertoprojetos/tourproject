import imp

from destiny.models import Destiny
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from season.models import Season

from .forms import (ActivityForm, ActivityPriceForm, CategoryPaxForm,
                    TripCategoryForm, TripForm)
from .models import (Activity, ActivityCatPax, ActivityPrice, CategoryPax,
                     Trip, TripCategory)


#===============================================================================
# CATEGORIA DE PASSEIO - TripCategory
class TripCategoryListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = TripCategory
    template_name = 'trip/trip_category_list_create.html'

    def get_context_data(self, **kwargs):
        context = super(TripCategoryListCreateView, self).get_context_data(**kwargs)
        context['form'] = TripCategoryForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TripCategoryForm(request.POST or None)

        if form.is_valid():
            form.save()
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
# PASSEIO - Trip
class TripListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
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
            messages.success(request, 'Passeio criado com sucesso!!!')
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

    def delete(self, request, *args, **kwargs):
        a = self.id
        return print(a)

trip_update = TripUpdateView.as_view()


class TripDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Trip
    template_name = 'trip/trip_delete.html'
    success_message = 'Passeio deletado com sucesso!!!'
    success_url = _('trip:trip_list_create')

    def delete(self, request, *args, **kwargs):
        return super(TripDeleteView, self).delete(request, *args, **kwargs)

trip_delete = TripDeleteView.as_view()


#===============================================================================
# CATEGORIA PAX - CategoryPax
class CategoryPAXListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = CategoryPax
    template_name = 'trip/categorypax_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryPAXListCreateView, self).get_context_data(**kwargs)
        context['form'] = CategoryPaxForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = CategoryPaxForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria PAX criada com sucesso!!!')
            return redirect('trip:categorypax_list_create')
        else:
            return render(request, 'trip/categorypax_list_create.html', {'object':'object','form': form})

categorypax_list_create = CategoryPAXListCreateView.as_view()


class CategoryPaxUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoryPax
    form_class = CategoryPaxForm
    template_name = 'trip/categorypax_update.html'
    success_message = 'Categoria PAX atualizada com sucesso!!!'
    success_url = _('trip:categorypax_list_create')

categorypax_update = CategoryPaxUpdateView.as_view()


class CategoryPaxDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoryPax
    template_name = 'trip/categorypax_delete.html'
    success_message = 'Categoria PAX deletada com sucesso!!!'
    success_url = _('trip:categorypax_list_create')

    def delete(self, request, *args, **kwargs):
        return super(CategoryPaxDeleteView, self).delete(request, *args, **kwargs)

categorypax_delete = CategoryPaxDeleteView.as_view()


#===============================================================================
# ATIVIDADES - Activity
class ActivityListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Activity
    template_name = 'trip/activity_list_create.html'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            trip__id=self.kwargs['trip_id']
        )

    def get_context_data(self, **kwargs):
        context = super(ActivityListCreateView, self).get_context_data(**kwargs)
        context['form'] = ActivityForm(self.request.POST or None)
        a=[]
        for i in self.object_list:
            a = i
        context['trip'] = a
        return context

    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST or None)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Atividade criada com sucesso!!!')
            # return redirect(_('trip:trip_option_list_create', kwargs={'trip_id': self.object.trip}))
            return redirect('trip:trip_list_create')
        else:
            context = {
                'form': form
            }
            return render(request, 'trip/activity_list_create.html', context)

activity_list_create = ActivityListCreateView.as_view()


class ActivityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = 'trip/activity_update.html'
    success_message = 'Atividade atualizada com sucesso!!!'

    def get_success_url(self):
        return _('trip:activity_list_create', kwargs={'trip_id': self.object.trip_id})

activity_update = ActivityUpdateView.as_view()


class ActivityDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Activity
    template_name = 'trip/activity_delete.html'
    success_message = 'Atividade deletada com sucesso!!!'

    def get_success_url(self):
        return _('trip:activity_list_create', kwargs={'trip_id': self.object.trip_id})

    def delete(self, request, *args, **kwargs):
        return super(ActivityDeleteView, self).delete(request, *args, **kwargs)

activity_delete = ActivityDeleteView.as_view()


#===============================================================================
# PREÇOS DOS PASSEIOS - ActivityPrice
class ActivityPriceListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = ActivityPrice
    template_name = 'trip/activity_price_list_create.html'
 
activity_price_list_create = ActivityPriceListView.as_view()

@login_required
def activity_price_update(request, trip_id):
    activity=Activity.objects.filter(trip_id=trip_id)
    trip=Trip.objects.filter(id=trip_id).first()
    activity_price_formset = modelformset_factory(ActivityPrice, form=ActivityPriceForm, extra=0)
    
    try:
        
        if activity.exists():

            # existe atividade(activity) para o passeio(trip)
            for a in activity:
                catpax=ActivityCatPax.objects.filter(activity_id=a.id)
                act_price=ActivityPrice.objects.filter(activity_id=a.id)
                season=Season.objects.filter(destiny_id=a.trip.destiny_id)

                # existe catpax para esta activity
                if catpax.exists():
                    cp_a=[]
                    cp_p=[]

                    # lista catpax da activity
                    for c in catpax:
                        cp_a.append(c.catpax_id)

                    if not act_price.exists():
                        for c in cp_a:                    
                            for s in season:
                                top = Activity.objects.get(id=a.id)
                                tca = CategoryPax.objects.get(id=c)
                                sea = Season.objects.get(id=s.id)
                                form = ActivityPrice(activity=top, catpax=tca, season=sea, price=0.00)
                                form.save()
                    else:
                        
                        # lista catpax_price da activity
                        for p in act_price:
                            cp_p.append(p.catpax_id)
                        cp_p_d=set(cp_a)-set(cp_p)
                        
                        # cria registro para cada activity, catpax, season, price
                        for c in cp_p_d:                    
                            for s in season:
                                top = Activity.objects.get(id=a.id)
                                tca = CategoryPax.objects.get(id=c)
                                sea = Season.objects.get(id=s.id)
                                form = ActivityPrice(activity=top, catpax=tca, season=sea, price=0.00)
                                form.save()

                else:
                    print('Não há CATPAX cadastrado para esta ACTIVITY!')

    except:
        messages.success(request, 'Cadastre ao menos uma "Atividade" antes de lançar valores.')
        return redirect(_('trip:trip_list_create'))
    
    # formulário para alteração de valores/ alteração dos npreços
    if request.method == 'POST':
        formset = activity_price_formset(request.POST, queryset=ActivityPrice.objects.filter(activity_id__trip_id=trip_id))

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, 'Valores alterados com sucesso!!!')
            return redirect('trip:activity_price_update', trip_id=trip_id)

    formset = activity_price_formset(queryset=ActivityPrice.objects.filter(activity_id__trip_id=trip_id))
    catpax=ActivityCatPax.objects.filter(activity_id__trip_id=trip_id)

    context = {
        'season':season,
        'catpax':catpax,
        'form':act_price,
        'activity':activity,
        'formset':formset,
        'trip':trip,
    }
    return render(request, 'trip/activity_price_update.html', context)

class ActivityPriceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ActivityPrice
    template_name = 'trip/activity_price_delete.html'
    success_message = 'Valor apagado com sucesso!!!'
    success_url = _('trip:activity_price_list')

    def delete(self, request, *args, **kwargs):
        return super(ActivityPriceDeleteView, self).delete(request, *args, **kwargs)

activity_price_delete = ActivityPriceDeleteView.as_view()
