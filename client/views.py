from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .forms import RegisterClientForm, EditClientForm
from .models import Client 


def client_register(request):
    form = RegisterClientForm()

    if request.method == 'POST':
        form = RegisterClientForm(request.POST or None)

        if form.is_valid():
            client = form.save(commit=True)
            return redirect('client:client_list')
        else:
            return render(request, 'client/client_create.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'client/client_create.html', {'form': form})

#update e delete precisa do int:pk
def client_edit(request, id):
    client = get_object_or_404(Client, id=id)
    form = EditClientForm(instance=client)    

    if request.method == 'POST':
        form = EditClientForm(request.POST or None,instance=client)        

        if form.is_valid():
            client = form.save(commit=True)
            return redirect('client:client_edit', client.id)
        else:
            return render(request, 'client/client_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'client/client_edit.html', {'form': form})

class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = "clients"


Client_list = ClientListView.as_view()

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_create.html'
    form_class = RegisterClientForm
    success_url = 'client:client_list'

	
Client_create = ClientCreateView.as_view()

