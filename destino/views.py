from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView
from .forms import RegisterDestinyForm, EditDestinyForm
from .models import Destiny 


#update e delete precisa do int:pk
def destiny_update(request, pk):
    destiny = get_object_or_404(Destiny, pk=pk)
    form = EditDestinyForm(instance=destiny)    

    if request.method == 'POST':
        form = EditDestinyForm(request.POST or None,instance=destiny)        

        if form.is_valid():
            destiny = form.save(commit=True)
            return redirect('destino:destiny_list')
        else:
            return render(request, 'destino/destiny_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'destino/destiny_edit.html', {'form': form})


class DeleteDestinyView(DeleteView):
    model = Destiny
    template_name = 'destino/destiny_delete.html'
    success_url = reverse_lazy('destino:destiny_list')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(DeleteDestinyView, self).delete(request, *args, **kwargs)


Destiny_Delete = DeleteDestinyView.as_view()

class DestinyListView(ListView):
    model = Destiny
    template_name = 'destino/destiny_list.html'
    context_object_name = "destinys"


Destiny_list = DestinyListView.as_view()

class DestinyCreateView(CreateView):
    model = Destiny
    template_name = 'destino/destiny_create.html'
    form_class = RegisterDestinyForm
    success_url = reverse_lazy('destino:destiny_list')

	
Destiny_register = DestinyCreateView.as_view()



