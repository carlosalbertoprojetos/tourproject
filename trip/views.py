from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import TripForm
from .models import Categories, Trip


class CategoryRegisterView(CreateView):
    model = Categories
    fields = '__all__'
    template_name = 'trip/category_register.html'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = _('trip:trip_list')


category_register = CategoryRegisterView.as_view()


class TripRegisterView(SuccessMessageMixin, CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_register.html'
    success_message = 'Passeio cadastrado com sucesso!!!'
    success_url = _('trip:trip_list')


trip_register = TripRegisterView.as_view()


class TripListView(ListView):
    model = Trip
    paginate_by = 4
    template_name = 'trip/trip_list.html'


trip_list = TripListView.as_view()


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trip/trip_details.html'


trip_details = TripDetailView.as_view()


class TripUpdateView(UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trip/trip_update.html'
    success_message = 'Passeio atualizado com sucesso!!!'
    success_url = _('trip:trip_list')


trip_update = TripUpdateView.as_view()


# class TripDeleteView(DeleteView):
#     model = Trip
#     template_name = 'trip/trip_delete.html'
#     success_url = _('trip:trip_list')

#     def delete(self, request, *args, **kwargs):
#         return super(TripDeleteView, self).delete(request, *args, **kwargs)


# trip_delete = TripDeleteView.as_view()
