import json
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy as _
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date

from .models import Package, Child_Package_One
from .forms import PackageForm,ChildAge_Factory ,PackageTrip_Factory

from trip.models import Activity, ActivityPrice, Trip
from destiny.models import Destiny
from season.models import Event
from package.models import PackageTrips



#===============================================================================
# DADOS PARA PACOTE - Data_package_One
# client => package

def data_package_list(request, id_destiny):
    destiny = Destiny.objects.filter(id=id_destiny).first()
    packages = Package.objects.filter(destiny_id=id_destiny)
    print(id_destiny)
    context = {
        'destiny': destiny,
        'packages': packages,
    }
    return render(request, 'package/data_package_list.html', context)

class DataPackageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Package
    template_name = 'package/data_package_delete.html'
    success_message = 'Pacote deletado com sucesso!!!'

    def get_success_url(self):
        return reverse('package:data_package_list', kwargs={'id_destiny': self.object.destiny_id})

    def delete(self, request, *args, **kwargs):
        return super(DataPackageDeleteView, self).delete(request, *args, **kwargs)

data_package_delete = DataPackageDeleteView.as_view()


@login_required
def children_ages_update(request, id_package):
    package=Package.objects.filter(id=id_package)
    # Child_Age_formset = modelformset_factory(Child_Package_One, form=Child_Package_OneForm, extra=0)
    destiny_id=[]
    destiny=[]
    for p in package:
        destiny_id = p.destiny_id
        destiny = p.destiny
    
    if request.method == 'POST':
        formset = ChildAge_Factory(request.POST, queryset=Child_Package_One.objects.filter(data_package_one=id_package))

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, 'Idade(s) alterada(s) com sucesso!!!')
            return redirect('package:data_package_list', id_destiny=destiny_id)

    formset = ChildAge_Factory(queryset=Child_Package_One.objects.filter(data_package_one=id_package))

    context = {
        'destiny': destiny,
        'package': package,
        'formset':formset,
    }
    return render(request, 'package/children_ages_update.html', context)


def data_base(request, city_destiny):
    object = Package.objects.filter(destiny__city=city_destiny).first()
    context = {
        'object': object,
        }
    return render(request, 'package/package_base.html', context)


def package(request, city_destiny):
    city = Destiny.objects.filter(city=city_destiny).first()
    destiny = Destiny.objects.filter(city=city_destiny).first()
    template = 'package/package_base.html'

    if request.method == 'GET':
        form = PackageForm()
        formset_ChildAge = ChildAge_Factory()
        formset_Trips = PackageTrip_Factory()       
        context = {
            'city': city,
            'form': form,
            'childformset': formset_ChildAge,
            'formset_trips': formset_Trips
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form = PackageForm(request.POST)
        formset_ChildAge = ChildAge_Factory(request.POST or None)
        formset_Trips = PackageTrip_Factory(request.POST or None)

        if form.is_valid() and formset_ChildAge.is_valid() and formset_Trips.is_valid():
            package = form.save(commit=False)
            package.destiny = destiny
            package.save()
            formset_ChildAge.instance = package
            formset_ChildAge.save()
            formset_Trips.instance = package
            formset_Trips.save()
            return redirect('package:package_concluded', package.id)
        else:
            context = {
                'city': city,
                'form': form,
                'childformset': formset_ChildAge,
                'formset_trips': formset_Trips
            }
            return render(request, template, context)


@csrf_exempt
def package_trips(request, city_destiny):

    st = request.POST.get('start_date')
    start_date = parse_date(st)
    ed = request.POST.get('end_date')
    end_date = parse_date(ed)
    city_destiny = request.POST.get('city_destiny')
    trips = Trip.objects.filter(destiny__city=city_destiny)

    events_exists = Event.objects.filter(Q(date_init__range=(start_date, end_date)) | Q(date_fin__range=(start_date, end_date)), season__destiny__city=city_destiny).first()
    if not events_exists:
        events = Event.objects.filter(season__destiny__city=city_destiny).first()
    else:
        events = events_exists

    activities = Activity.objects.filter(trip__destiny__city=city_destiny)
    activities_prices = ActivityPrice.objects.filter(season__id=events.season.id, activity__trip__destiny__city=city_destiny)
    len_prices = len(activities_prices)

    template = 'package/includes/package_trips.html'
    context = {
        'len_prices': json.dumps(len_prices),

        'trips': trips,
        'activities': activities,
        'activities_prices': activities_prices,
        }
    return render(request, template, context)

@csrf_exempt
def package_accommodation(request, city_destiny):
    # st = request.POST.get('start_date')
    # start_date = parse_date(st)
    # ed = request.POST.get('end_date')
    # end_date = parse_date(ed)
    city_destiny = request.POST.get('city_destiny')
    trips = Trip.objects.filter(destiny__city=city_destiny)
    # import pdb;pdb.set_trace()

    template = 'package/includes/package_accommodation.html'
    context = {
        'trips': trips,
        }
    return render(request, template, context)


@csrf_exempt
def package_transport(request, city_destiny):
    # st = request.POST.get('start_date')
    # start_date = parse_date(st)
    # ed = request.POST.get('end_date')
    # end_date = parse_date(ed)
    city_destiny = request.POST.get('city_destiny')
    trips = Trip.objects.filter(destiny__city=city_destiny)

    template = 'package/includes/package_transport.html'
    context = {
        'trips': trips,
        }
    return render(request, template, context)




def package_concluded(request, id_package=4):

    num_adults = 0
    num_child = 0
    package = Package.objects.filter(id=id_package)
    for p in package:
        num_adults = p.num_adults
        num_child = p.num_child

    packtrips = PackageTrips.objects.filter(package_id=id_package)
    pacote = []
    total = 0

    for pk in packtrips:
        trip = pk.id_price.activity.trip.name
        activity = pk.id_price.activity.name
        catpax = pk.id_price.catpax.name
        valor = 0
        amount = 0
        price = 0

        if (pk.id_price.catpax.name == 'Criança') or (pk.id_price.catpax.name == 'CHD'):
            amount = num_child
            valor = float(pk.id_price.price)
            price = (num_child * valor)
        else:
            amount = num_adults
            valor = float(pk.id_price.price)
            price = (num_adults * valor)

        pacote.append({'trip':trip,'activity': activity, 'catpax': catpax, 'valor': valor, 'amount': amount, 'price': price})
        total += price

    template = 'package/package_concluded.html'
    context = {
        'total': total,
        'pacote': pacote,
        'total': total,
        'package': package,
    }

    return render(request, template, context)