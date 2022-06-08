import imp
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from django.contrib.auth.decorators import login_required

from season.models import Season

from .models import (ActivityCatPax, TripCategory, Trip, CategoryPax, Activity,
                     ActivityPrice)
from .forms import (TripCategoryForm, TripForm, CategoryPaxForm,
                    ActivityForm, ActivityPriceForm)


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


def activity_price_update_tr(trip_id=2):

    trip=Trip.objects.filter(id=trip_id)
    activity=Activity.objects.filter(trip_id=trip_id)
    catpax= ActivityCatPax.objects.all()
    season=Season.objects.all()

    for t in trip:
        print('TRIP', t.id)
        for a in activity:
            print(f'  ATIVIDADE {a.id}')
            for c in catpax:
                if c.activity_id == a.id:
                    print(f'    CATPAX {c.id}')
                    for s in season:
                        if t.destiny_id == s.destiny_id:
                            print(f'      SEASON {s.id}')
    

                            # print(f'TO {b.id}, CA {c}, TE {d.id}')
                            # top = Activity.objects.get(id=b)
                            # tca = CategoryPax.objects.get(id=c)
                            # sea = Season.objects.get(id=d.id)
                            # form = ActivityPrice(activity=top, catpax=tca, season=sea, price=0.00)
                            # form.save()

activity_price_update_tr()

""" 
@login_required
def activity_price_update_tr(request, trip_id):
    activity = Activity.objects.filter(trip_id=trip_id)

    try:
        if activity != '':
            activity_price_formset = modelformset_factory(ActivityPrice, form=ActivityPriceForm, extra=0)

            catpax=[]
            season=[]
            trip=[]

            for a in activity:
                trip=a.trip
                tp = ActivityPrice.objects.filter(activity_id__trip_id=a.trip_id)
                for i in tp:
                    if i.activity_id == a.id:
                        catpax.append(i.catpax)
                        season.append(i.season)

            catpax=list(set(catpax))
            season=list(set(season))

            if request.method == 'POST':
                formset = activity_price_formset(request.POST, queryset=ActivityPrice.objects.filter(activity_id__trip_id=a.trip_id))

                if formset.is_valid():
                    instances = formset.save(commit=False)
                    for instance in instances:
                        instance.save()
                    messages.success(request, 'Valores alterados com sucesso!!!')
                    return redirect('trip:activity_price_update_tr', trip_id=a.trip_id)

            formset = activity_price_formset(queryset=ActivityPrice.objects.filter(activity_id__trip_id=a.trip_id))

            context = {
                'season':season,
                'cadpax':catpax,
                'activity':activity,
                'formset':formset,
                'trip':trip,
            }
            return render(request, 'trip/activity_update_tr.html', context)

    except:
        messages.success(request, 'Cadastre "Atividades" antes de lançar valores.')
        return redirect(_('trip:trip_list_create'))

"""

@login_required
def activity_price_update(request, activity_id):
    activity = Activity.objects.filter(id=activity_id)

    activity_price = ActivityPrice.objects.filter(trip_activity_id=activity_id)
    trip_price_formset = modelformset_factory(ActivityPrice, form=ActivityPriceForm, extra=0)

    cadpaxs=[]
    seasons=[]
    activities=[]
    for i in activity_price:
        cadpaxs.append(i.cadpax)
        seasons.append(i.season)
        if not i.trip_activity_id in activities:
            activities.append(i.trip_activity_id)

    activities=list((activities))
    cadpaxs=list(set(cadpaxs))
    seasons=list(set(seasons))

    if request.method == 'POST':
        formset = trip_price_formset(request.POST, queryset=ActivityPrice.objects.filter(trip_activity_id=activity_id))

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()

            messages.success(request, 'Valores alterados com sucesso!!!')
            return redirect('trip:activity_price_update', activity_id)

    formset = trip_price_formset(queryset=ActivityPrice.objects.filter(
        activity_id=activity_id))

    context = {
        'season':seasons,
        'cadpax':cadpaxs,
        'activity':activity,
        'formset':formset
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

""" 
def tripteste(trip_option_id=11):
    t=[]
    trip = []
    to=[]
    tripOption = []
    tp=[]
    tpz=[]
    b=[]
    bz=[]
    s=[]
    criar = []
    deletar = []
    tz=[]
    print('=='*50)

    trip_option = TripOption.objects.filter(id=trip_option_id)
    for i in trip_option:
        to = i.id
        tripOption = i.name
        t = i.trip_id
        trip = i.trip

    tripcadpax = TripCadPaxTrip.objects.all()
    for i in tripcadpax:
        if i.trip_id == t:
            b.append(i.cadpax_id)
            bz.append((i.id, i.cadpax_id))

    tripprice = TripPrice.objects.all()
    for i in tripprice:
        if i.trip_option_id == to:
            s.append(i.season_id)
            tz.append((i.season_id, i.cadpax_id))
            tp.append(i.cadpax_id)
            tpz.append((i.id, i.cadpax_id))
   
    st = s
    season_trip = set(st)
    # print(season)
    # lista das cadpax no model trip_cadpax_trip existentes para determinada trip
    tc_t = set(b)

    # lista de objetos cadpax no model trip_price existentes para determinada trip, atraves do trip_option
    tc_tp = set(tp)

    print(f'TRIP: {trip} - ID:{t}')
    print(f'TRIP Option: {tripOption} - ID:{to}')

    print('TCT', tc_t)
    print('TCP', tc_tp)
    print('TZ', tz)
    

    test = [1]
    # está criando apenas uma season

    if test:
        print('Objeto(s) a ser(em) criado(s):')
        for z in season_trip:
            for ta in tc_t:
                if not ta in tc_tp:
                    criar.append(ta)
                    print(f'cadpax: {ta} season: {z} tp: {to}')
                    top = TripOption.objects.get(id=to)
                    ta = TripCategoryPax.objects.get(id=ta)
                    z = season = Season.objects.get(id=z)
                    form = TripPrice(trip_option=top, cadpax=ta, season=z, price=0.00) 
                    form.save()

        for z in season_trip:
            for tp in tc_tp:
                if not tp in tc_t:
                    deletar.append(tp)
                    print('Objeto(s) a ser(em) deletado(s):')
                    for z in season_trip:
                        print(f'cadpax: {tp} season: {z} tp: {to}')
                        ab = TripPrice.objects.all()
                        id = []
                        for i in ab:
                            if i.trip_option_id == to and i.cadpax.id == tp:
                                id.append(i.id)
                                print(i.id)
                        
                        # for i in id:
                        #     record = TripPrice.objects.get(id = i)
                        #     record.delete()

        print('termo(s) igual(is)', tc_t & tc_tp)
    else:
        print('São iguais!!!')

    dif = []
    cr=[]
    de=[]
    for i in criar:
        dif.append(i)
        cr = i
    for i in deletar:
        dif.append(i)
        de = i

    print('termo(s) diferente(s)', dif)
    print('=='*50)


# tripteste()
 """

def teste(id):
    # filtro atividades por trip
    trip=Trip.objects.filter(id=id)    
    activity=Activity.objects.all()
    catpax=ActivityCatPax.objects.all()
    season=Season.objects.all()

    # se há atividade para a trip e individualiza cada catpax da atividade
    for t in trip:
        print('TRIP', t.id)
        for a in activity:
            print(f'  ATIVIDADE {a.id}')
            for c in catpax:
                if a.id == c.activity_id:
                    print(f'    CATPAX {c.id}')
                    for s in season:
                        if t.destiny_id == s.destiny_id:
                            print(f'      SEASON {s.id}')
                            # print(f'TO {b.id} , CA {c.catpax_id}, TE {d.id}')
                            top = Activity.objects.get(id=b.id)
                            tca = CategoryPax.objects.get(id=c.catpax_id)
                            sea = Season.objects.get(id=d.id)
                            form = ActivityPrice(activity=top, catpax=tca, season=sea, price=0.00)
                            form.save()
# teste(1)