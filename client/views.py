from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import ClientForm
from .models import Client


class ClientListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Client
    template_name = 'client/client_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(ClientListCreateView, self).get_context_data(**kwargs)
        context['form'] = ClientForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Transporte criado com sucesso!!!')
            return redirect('client:client_list_create')
        else:
            return render(request, 'client/client_list_create.html', {'object':'object','form': form})

client_list_create = ClientListCreateView.as_view()


class ClientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client/client_edit.html'
    success_message = 'Dados do cliente alterados com sucesso!!!'
    success_url = _('client:client_list_create')

client_update = ClientUpdateView.as_view()


class ClientDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_message = 'Cliente deletado com sucesso!'
    success_url = _('client:client_list_create')

    def delete(self, request, *args, **kwargs):        
        return super(ClientDeleteView, self).delete(request, *args, **kwargs)

client_delete = ClientDeleteView.as_view()
