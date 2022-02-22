from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
#from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .forms import RegisterClientForm
from .models import Client 

def client_list(request):
	list_client = Client.objects.all()	
	return render(request, "client_list.html", {"client":list_client})


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'

client_list = ClientListView.as_view()


