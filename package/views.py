from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory, modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy as _
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView

from .models import Data_Package_One, Child_Package_One
from .forms import Data_Package_OneForm, Child_Package_OneForm

from destiny.models import Destiny



#===============================================================================
# DADOS PARA PACOTE - Data_package_One
# client => package


def data_package_create(request, id_destiny):
    destiny = Destiny.objects.filter(id=id_destiny).first()
    Formset_Factory = inlineformset_factory(
    Data_Package_One, Child_Package_One, fields=('children_age',), extra=0, can_delete=False)

    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None)
        formset = Formset_Factory(request.POST or None)
        
        if form.is_valid() and formset.is_valid():
            package = form.save(commit=False)
            package.destiny = destiny
            package.save()
            formset.instance = package
            formset.save()
            return redirect('package:data_package_list', id_destiny )
        else:
            context = {
                'destiny': destiny,
                'form': form,
                'formset': formset,
            }    
            return render(request, 'destiny/destiny_list_create.html', context)

    elif request.method == 'GET':
        form = Data_Package_OneForm()
        formset = Formset_Factory()
        
        context = {
            'destiny': destiny,
            'form': form,
            'formset': formset,
        }   
        return render(request, 'package/data_package_create.html', context)


def data_package_list(request, id_destiny):
    destiny = Destiny.objects.filter(id=id_destiny).first()
    object = Data_Package_One.objects.filter(destiny_id=id_destiny)
    
    context = {
        'destiny': destiny,
        'object': object,
    }
    return render(request, 'package/data_package_list.html', context)

class DataPackageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Data_Package_One
    template_name = 'package/data_package_delete.html'
    # success_message = 'deletada com sucesso!!!'

    def get_success_url(self):
        return reverse('package:data_package_list', kwargs={'id_destiny': self.object.destiny_id})

    def delete(self, request, *args, **kwargs):
        return super(DataPackageDeleteView, self).delete(request, *args, **kwargs)

data_package_delete = DataPackageDeleteView.as_view()



"""
class DataPackageOneListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Data_Package_One
    form_class = Data_Package_OneForm
    template_name = 'package/data_package_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(DataPackageOneListCreateView, self).get_context_data(**kwargs)
        context['form'] = Data_Package_OneForm(self.request.POST or None)
        context['destiny'] = Destiny.objects.filter(id=self.kwargs['id_destiny'])
        context['object'] = Data_Package_One.objects.filter(destiny_id=self.kwargs['id_destiny'])
        return context

    # def get_queryset(self):
    #     return Data_Package_One.objects.filter(destiny_id=self.kwargs['id_destiny'])

     def post(self, request, *args, **kwargs):
        destiny = Destiny.objects.filter(id=self.kwargs['id_destiny'])
        
        form = Data_Package_OneForm(request.POST or None)
        
        Formset_Factory = inlineformset_factory(
        Data_Package_One, Child_Package_One, fields=('children_age',), extra=3, can_delete=False)
        formset = Formset_Factory(request.POST or None)
        
        if form.is_valid() and formset.is_valid():
            package = form.save(commit=False)
            package.save()
            formset.instance = package
            formset.save()
            messages.success(request, 'Pacote criado com sucesso!!!')
            return redirect('package:data_package_create')
        else:
            context = {
                'destiny': destiny,
                'form': form,
                'formset': formset,
            }    
        return render(request, 'destiny/destiny_list_create.html', context)

data_package_list = DataPackageOneListCreateView.as_view() """