
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import EditTransportForm, RegisterTransportForm
from .models import Transport


class TransortRegisterView(SuccessMessageMixin, CreateView):
    model = Transport
    form_class = RegisterTransportForm
    template_name = 'transport/transport_register.html'
    success_message = 'Transporte cadastrado com sucesso!!!'
    success_url = _('transport:transport_list')


transport_register = TransortRegisterView.as_view()



# def transport_register(request):
#     form = RegisterTransportForm()

#     if request.method == 'POST':
#         form = RegisterTransportForm(request.POST or None)

#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('transport:transport_list')
#         else:
#             return render(request, 'transport/transport_create.html', {'form': form})

#     elif request.method == 'GET':
#         return render(request, 'transport/transport_create.html', {'form': form})


class TransportUpdateView(UpdateView):
    model = Transport
    form_class = RegisterTransportForm
    template_name = 'transport/transport_edit.html'
    success_message = 'Dados alterados com sucesso!!!'
    success_url = _('transport:transport_list')

transport_update = TransportUpdateView.as_view()



#update e delete precisa do int:pk
# def transport_update(request, pk):
#     transport = get_object_or_404(Transport, pk=pk)
#     form = EditTransportForm(instance=transport)    

#     if request.method == 'POST':
#         form = EditTransportForm(request.POST or None,instance=transport)        

#         if form.is_valid():
#             transport = form.save(commit=True)
#             return redirect('transport:transport_list')
#         else:
#             return render(request, 'transport/transport_edit.html', {'form': form})

#     elif request.method == 'GET':
#         return render(request, 'transport/transport_edit.html', {'form': form})


class DeletarTransporteView(DeleteView):
    model = Transport
    template_name = 'transport/transport_delete.html'
    success_url = _('transport:transport_list')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(DeletarTransporteView, self).delete(request, *args, **kwargs)


Transport_Delete = DeletarTransporteView.as_view()


class TransportListView(ListView):
    model = Transport
    template_name = 'transport/transport_list.html'
    context_object_name = "transports"


Transport_list = TransportListView.as_view()

