from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView


from .forms import EditClientForm, RegisterClientForm
from .models import Client


class ClientRegisterView(SuccessMessageMixin, CreateView):
    model = Client
    form_class = RegisterClientForm
    template_name = 'client/client_create.html'
    success_message = 'Cliente cadastrado com sucesso!!!'
    success_url = _('client:client_list')


client_register = ClientRegisterView.as_view()


# def client_register(request):
#     form = RegisterClientForm()

#     if request.method == 'POST':
#         form = RegisterClientForm(request.POST or None)

#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('client:client_list')
#         else:
#             return render(request, 'client/client_create.html', {'form': form})

#     elif request.method == 'GET':
#         return render(request, 'client/client_create.html', {'form': form})



class ClientUpdateView(UpdateView):
    model = Client
    form_class = RegisterClientForm
    template_name = 'client/client_edit.html'
    success_message = 'Dados alterados com sucesso!!!'
    success_url = _('client:client_list')

client_edit = ClientUpdateView.as_view()


#update e delete precisa do int:pk
# def client_edit(request, id):
#     client = get_object_or_404(Client, id=id)
#     form = EditClientForm(instance=client)    

#     if request.method == 'POST':
#         form = EditClientForm(request.POST or None,instance=client)        

#         if form.is_valid():
#             client = form.save(commit=True)
#             return redirect('client:client_edit', client.id)
#         else:
#             return render(request, 'client/client_edit.html', {'form': form})

#     elif request.method == 'GET':
#         return render(request, 'client/client_edit.html', {'form': form})


class ClientListView(ListView):
    model = Client
    template_name = 'client/client_list.html'
    context_object_name = "clients"


Client_list = ClientListView.as_view()

