from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import DestinyForm
from .models import Destiny



class DestinyListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Destiny
    form_class = DestinyForm
    template_name = 'destiny/destiny_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(DestinyListCreateView, self).get_context_data(**kwargs)
        context['form'] = DestinyForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = DestinyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Destino criado com sucesso!!!')
            return redirect('destiny:destiny_list_create')
        else:
            return render(request, 'destiny/destiny_list_create.html', {'object':'object','form': form})

destiny_list_create = DestinyListCreateView.as_view()

class DestinyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Destiny
    form_class = DestinyForm
    template_name = 'destiny/destiny_update.html'
    success_message = 'Destino atualizado com sucesso!!!'
    success_url = _('destiny:destiny_list_create')


destiny_update = DestinyUpdateView.as_view()


class DestinyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Destiny
    template_name = 'destiny/destiny_delete.html'
    success_url = _('destiny:destiny_list_create')
    success_message = 'Deletado com sucesso!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DestinyDeleteView, self).delete(request, *args, **kwargs)


destiny_delete = DestinyDeleteView.as_view()



