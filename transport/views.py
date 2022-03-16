
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView
from .forms import RegisterTransportForm, EditTransportForm
from .models import Transport 


#update e delete precisa do int:pk
def transport_update(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    form = EditTransportForm(instance=transport)    

    if request.method == 'POST':
        form = EditTransportForm(request.POST or None,instance=transport)        

        if form.is_valid():
            transport = form.save(commit=True)
            return redirect('transport:transport_list')
        else:
            return render(request, 'transport/transport_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'transport/transport_edit.html', {'form': form})


class DeletarTransporteView(DeleteView):
    model = Transport
    template_name = 'transport/transport_delete.html'
    success_url = reverse_lazy('transport:transport_list')
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

class TransportCreateView(CreateView):
    model = Transport
    template_name = 'transport/transport_create.html'
    form_class = RegisterTransportForm
    success_url = reverse_lazy('transport:transport_list')
    
Transport_register = TransportCreateView.as_view()



