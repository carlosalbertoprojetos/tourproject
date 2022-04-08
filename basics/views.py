from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages


from .models import CategoryPax
from .forms import CategoryPaxForm



# ------------------------- CATEGORIA PAX  -------------------------

class CategoryPAXListCreateView(LoginRequiredMixin, ListView):
    model = CategoryPax
    template_name = 'basics/categorypax_list_create.html'
    
    def get_context_data(self, **kwargs):
        context = super(CategoryPAXListCreateView, self).get_context_data(**kwargs)
        context['form_catpax'] = CategoryPaxForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form_cat = CategoryPaxForm(request.POST or None)

        if form_cat.is_valid():
            form_cat.save(commit=True)
            messages.success(request, 'Categoria criada com sucesso!!!')
            return redirect('basics:categorypax_list_create')
        else:
            return render(request, 'basics/categorypax_list_create.html', {'object':'object','form_catpax': form_cat})

categorypax_list_create = CategoryPAXListCreateView.as_view()


class CategoryPaxUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoryPax
    form_class = CategoryPaxForm
    template_name = 'basics/categorypax_update.html'
    success_message = 'Categoria atualizada com sucesso!!!'
    success_url = _('basics:categorypax_list_create')

categorypax_update = CategoryPaxUpdateView.as_view()


class CategoryPaxDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoryPax
    template_name = 'basics/categorypax_delete.html'
    success_message = 'Categoria deletada com sucesso!!!'
    success_url = _('basics:categorypax_list_create')

    def delete(self, request, *args, **kwargs):
        return super(CategoryPaxDeleteView, self).delete(request, *args, **kwargs)

categorypax_delete = CategoryPaxDeleteView.as_view()