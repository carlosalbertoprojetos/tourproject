from operator import length_hint
from re import template
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory, modelformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy as _
from django.views import View
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date

from .models import Data_Package_One, Child_Package_One
from .forms import Data_Package_OneForm, Child_Package_OneForm, Formset_Factory, Child_Age_formset, Child_Formset_Factory, Chosen_Formset_Factory

from trip.models import Activity, ActivityPrice, Trip
from destiny.models import Destiny
from season.models import Event, Season


#===============================================================================
# DADOS PARA PACOTE - Data_package_One
# client => package

def data_package_list(request, id_destiny):
    destiny = Destiny.objects.filter(id=id_destiny).first()
    packages = Data_Package_One.objects.filter(destiny_id=id_destiny)

    context = {
        'destiny': destiny,
        'packages': packages,
    }
    return render(request, 'package/data_package_list.html', context)


def data_package_create(request, id_destiny):
    destiny = Destiny.objects.filter(id=id_destiny).first()
    # Formset_Factory = inlineformset_factory(
    # Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)

    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None)
        formset = Formset_Factory(request.POST or None)

        if form.is_valid() and formset.is_valid():
            package = form.save(commit=False)
            package.destiny = destiny
            package.save()
            formset.instance = package
            formset.save()
            return redirect('package:listTripPackage', id_destiny )
        else:
            context = {
                'destiny': destiny,
                'form': form,
                'formset': formset,
            }    
            return render(request, 'destiny/destiny_list_create.html', context)

    elif request.method == 'GET':
        form = Data_Package_OneForm()
        formset = Formset_Factory()
        
        context = {
            'destiny': destiny,
            'form': form,
            'formset': formset,
        }   
        return render(request, 'package/data_package_create.html', context)


def data_package_create1(request, city_destiny):
    destiny = Destiny.objects.filter(city=city_destiny).first()
    # Formset_Factory = inlineformset_factory(
    # Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)

    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None)
        formset = Formset_Factory(request.POST or None)
        
        if form.is_valid() and formset.is_valid():
            package = form.save(commit=False)
            package.destiny = destiny
            package.save()
            formset.instance = package
            formset.save()
            return redirect('package:listTripPackage', city_destiny)
        else:
            context = {
                'destiny': destiny,
                'form': form,
                'formset': formset,
            }    
            return render(request, 'package/package_base.html', context)

    elif request.method == 'GET':
        form = Data_Package_OneForm()
        formset = Formset_Factory()
        
        context = {
            'destiny': destiny,
            'form': form,
            'formset': formset,
        }   
        return render(request, 'package/package_base.html', context)


class DataPackageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Data_Package_One
    template_name = 'package/data_package_delete.html'
    success_message = 'Pacote deletado com sucesso!!!'

    def get_success_url(self):
        return reverse('package:data_package_list', kwargs={'id_destiny': self.object.destiny_id})

    def delete(self, request, *args, **kwargs):
        return super(DataPackageDeleteView, self).delete(request, *args, **kwargs)

data_package_delete = DataPackageDeleteView.as_view()


@login_required
def children_ages_update(request, id_package):
    package=Data_Package_One.objects.filter(id=id_package)
    # Child_Age_formset = modelformset_factory(Child_Package_One, form=Child_Package_OneForm, extra=0)
    destiny_id=[]
    destiny=[]
    for p in package:
        destiny_id = p.destiny_id
        destiny = p.destiny
    
    if request.method == 'POST':
        formset = Child_Age_formset(request.POST, queryset=Child_Package_One.objects.filter(data_package_one=id_package))

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, 'Idade(s) alterada(s) com sucesso!!!')
            return redirect('package:data_package_list', id_destiny=destiny_id)

    formset = Child_Age_formset(queryset=Child_Package_One.objects.filter(data_package_one=id_package))

    context = {
        'destiny': destiny,
        'package': package,
        'formset':formset,
    }
    return render(request, 'package/children_ages_update.html', context)


def data_base(request, city_destiny):
    object = Data_Package_One.objects.filter(destiny__city=city_destiny).first()
    context = {
        'object': object,
        }
    return render(request, 'package/package_base.html', context)


def package(request, city_destiny):
    
    city = Destiny.objects.filter(city=city_destiny).first()
    # trips = Trip.objects.filter(destiny__city=city_destiny)
    # activities = Activity.objects.filter(trip__destiny__name=city_destiny)
    # season = Season.objects.filter(destiny__city=city_destiny)

    # season = Season.objects.filter(destiny__city=city_destiny)
    # events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
    # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season__id=events.season.id)
    # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny)

    # for t in trips:
    #     print(t)
    #     activities = Activity.objects.filter(trip=t)
    #     for a in activities:
    #         print('  ', a)
    #         events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
    #         activities_prices = ActivityPrice.objects.filter(activity_id=a.id, season__id=events.season.id)
    #         for p in activities_prices:
    #             print('    ', p.catpax, p.price)

    template = 'package/package_base.html'

    destiny = Destiny.objects.filter(city=city_destiny).first()
    # Child_Formset_Factory = inlineformset_factory(
    # Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)
    # Chosen_Formset_Factory = inlineformset_factory(
    # Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)
    form = Data_Package_OneForm()
    formset = Child_Formset_Factory()

    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None)
        formset = Child_Formset_Factory(request.POST or None)
        
        """ 
        # # st = form.data['start_date']
        start_date = parse_date(form.data['start_date'])
        # # ed = form.data['end_date']
        end_date = parse_date(form.data['end_date'])

        # trips = Trip.objects.filter(destiny__city=city_destiny)
        # activities = Activity.objects.filter(trip__destiny__name=city_destiny)
        # import pdb;pdb.set_trace()
        # season = Season.objects.filter(destiny__city=city_destiny)

        events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
        # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season__id=events.season.id)
        activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny)

        for t in trips:
            print(t)
            activities = Activity.objects.filter(trip=t)
            for a in activities:
                print('  ', a)
                events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
                # activities_prices = ActivityPrice.objects.filter(activity_id=a.id, season__id=events.season.id)
                activities_prices = ActivityPrice.objects.filter(activity_id=a.id)
                for p in activities_prices:
                    print('    ', p.catpax, p.price)

        # start_date = form.POST.get['date_arrive']
        # end_date = form.POST.get['date_departure']
        # print('início:', start_date,'\n', 'fim:', end_date)

        # start_date = form.cleaned_data['date_arrive']
        # end_date = form.cleaned_data['date_departure']
        # print('início:', start_date,'\n', 'fim:', end_date)

        # filterform=form.cleaned_data

        # start_date = request.POST.get['date_arrive']
        # end_date = request.POST.get['date_departure']
        # print('início:', start_date,'\n', 'fim:', end_date)
        
        # events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season=season).first()
        # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season=events.season)
        # for a in activities_prices:
        #     print(a)        

        # events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
        # print(events)
        # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season__id=events.season.name)
        # for p in activities_prices:
        #     print(p, ' R$', p.price)

        # if (Q(form.POST.get['name']) | Q(form.POST.get['email']) | Q(form.POST.get['city']) | Q(form.POST.get['description']) | Q(form.POST.get['phonenumber'])) == '':
        # if all(form.is_valid(), Childformset.is_valid(), Chosenformset.is_valid()):
        """
        
        if form.is_valid() and formset.is_valid():
            # if todos os dados estao preenchidos:
            #     package = form.save(commit=False)
            # else:
            #     return formulario parcial

            package = form.save(commit=False)
            package.destiny = destiny
            # package=package.cleaned_data

            # start_date = request.POST.get['date_arrive']
            # end_date = request.POST.get['date_departure']
            # print('início:', start_date,'\n', 'fim:', end_date)

            # date_arrive = package['date_arrive']
            # date_departure = package['date_departure']
            # print('início:', date_arrive, 'fim:', date_departure)

            # events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season=season).first()
            # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season=events.season)
            # print(activities_prices)
            
            formset.instance = package
            # Chosenformset.instance = package
            # package.save()
            # formset.save()
            # Chosenformset.save()
            return redirect('package:package', city_destiny)
        else:
            context = {
                'city': city,
                # 'trips': trips,
                # 'activities': activities,
                # 'activities_prices': activities_prices,
                'form': form,
                'Childformset': formset,
                # 'Chosenformset': Chosenformset
            }
            return render(request, template, context)

    elif request.method == 'GET':
        # form = Data_Package_OneForm()
        # formset = Child_Formset_Factory()
        # Chosenformset = Chosen_Formset_Factory()
        
        # start_date = request.GET.get('start_date')
        # end_date = request.GET.get('end_date')
        # sd = request.GET.get('start_date')
        # start_date = parse_date(sd)
        # ed = request.GET.get('end_date')
        # end_date = parse_date(ed)
        # print(start_date, end_date)
        # print('Destino: ', start_date)
        # events = Event.objects.filter(season__destiny__city=city_destiny)
        # print(events)
        # for e in events:
        #     print(e.season)
        # if events is None:
        #     seasonev = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
        #     print(seasonev)
        #     print('SIM, EXISTE EVENTO PARA O PERÍODO.\n')
        # else:
        # seasonev = Event.objects.latest('season').season
            # print('NÃO EXISTE EVENTO PARA O PERÍODO.')

        # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season__id=seasonev.id)
        # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny)

        """
        for t in trips:
            print(t)
            activities = Activity.objects.filter(trip=t)
            for a in activities:
                print('  ', a)
                # events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
                seasonev = Event.objects.latest('season').season
                print(seasonev)
                activities_prices = ActivityPrice.objects.filter(activity_id=a.id, season__id=seasonev.id)
                # activities_prices = ActivityPrice.objects.filter(activity_id=a.id)
                for p in activities_prices:
                    print('    ', p.catpax, p.price)
        """

        # caso não tenha evento para o período:
        # último evento cadastrado para o destino
        # events = Event.objects.latest('season', 'pk').season.pk

        context = {
                'city': city,
                # 'trips': trips,
                # 'activities': activities,
                # 'activities_prices': activities_prices,
                'form': form,
                'Childformset': formset,
                # 'Chosenformset': Chosenformset
        }
        return render(request, template, context)


    """ 
    def list_activities_package(request, city_destiny):
        # city_destiny = request.city_destiny
        
        context = {'start_date': None, 'end_date': None}
        if request.method == 'POST':
            form = Data_Package_OneForm(request.POST or None)
            start_date = parse_date(form.data['start_date'])
            end_date = parse_date(form.data['end_date'])

            context = {
                'start_date': start_date,
                'end_date': end_date
            }
            import pdb;pdb.set_trace()

        return JsonResponse(context)

    """

from datetime import datetime

@csrf_exempt
def package_trips(request, city_destiny):

    st = request.POST.get('start_date')
    start_date = parse_date(st)
    ed = request.POST.get('end_date')
    end_date = parse_date(ed)
    city_destiny = request.POST.get('city_destiny')

    trips = Trip.objects.filter(destiny__city=city_destiny)

    activities = Activity.objects.filter(trip__destiny__name=city_destiny)
    season = Season.objects.filter(destiny__city=city_destiny)

    events_exists = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
    if not events_exists:
        events = Event.objects.filter(season__destiny__city=city_destiny).first()
    else:
        events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
        
    print(events)
    activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season__id=events.season.id)
    # activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny)


    """     
    for t in trips:
        print(t)
        # activities = Activity.objects.filter(trip=t)
        for a in activities:
            print('  ', a)
            # events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
            # activities_prices = ActivityPrice.objects.filter(activity_id=a.id, season__id=events.season.id)
            # activities_prices = ActivityPrice.objects.filter(activity_id=a.id)
            for p in activities_prices:
                    print('    ', p.catpax, p.price)
    """

    template = 'package/includes/package_trips_list.html'
    context = {
        'trips': trips,
        'activities': activities,
        'activities_prices': activities_prices,
        }
    return render(request, template, context)


# city_destiny = request.city
# if request.is_ajax():        
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')
    
#     # start_date = dt.date(2023, 1, 1)
#     # end_date = dt.date(2023, 12, 28)
#     trips = Trip.objects.filter(destiny__city=city_destiny)
#     activities = Activity.objects.filter(trip__destiny__name=city_destiny)
#     # season = Season.objects.filter(destiny__city=city_destiny)
#     events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
#     activities_prices = ActivityPrice.objects.filter(activity__trip__destiny__city=city_destiny, season__id=events.season.id) 

#     for t in trips:
#         print(t)
#         activities = Activity.objects.filter(trip=t)
#         for a in activities:
#             print('  ', a)
#             events = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
#             activities_prices = ActivityPrice.objects.filter(activity_id=a.id, season__id=events.season.id)
#             for p in activities_prices:
#                 print('    ', p.catpax, p.price)

#     template = 'package/package_base.html'
#     context = {
#                 'trips': trips,
#                 'activities': activities,
#                 'activities_prices': activities_prices,
#                 # 'Chosenformset': Chosenformset
#     }
#     return render(request, template, context)


# class DataCustomerPackageCreateView(SuccessMessageMixin, CreateView):
#     model = Data_Customer_Package
#     form_class = Data_Customer_PackageForm
#     template_name = 'package/package_base.html'
#     # success_message = 'Cadastrado com sucesso!'

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.package = self.package
#         obj.save()
#         return super().form_valid(form)

# data_customer_package_create = DataCustomerPackageCreateView.as_view()


# class DataCustomerPackageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Data_Customer_Package
#     form_class = Data_Customer_PackageForm
#     success_message = 'Editado com sucesso!'

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.package = self.package
#         obj.save()
#         return super().form_valid(form)


# data_customer_package_update = DataCustomerPackageUpdateView.as_view()


# class DataCustomerPackageDeleteView(DeleteView):
#     model = Data_Customer_Package
#     template_name = 'reinosdeferro/deletar_post.html'
#     success_url = _('')
#     success_message = 'Deletado com sucesso!'

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request,self.success_message)
#         return super(DataCustomerPackageDeleteView, self).delete(request, *args, **kwargs)


# data_customer_package_delete = DataCustomerPackageDeleteView.as_view()

def teste():
        activities_prices = ActivityPrice.objects.all()
        # Chosenformset = Chosen_Formset_Factory(request.POST or None)
        for p in activities_prices:
            print(p, ' R$', p.price)

# teste()