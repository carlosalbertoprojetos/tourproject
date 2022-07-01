from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory, modelform_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy as _
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import Data_Package_One, Child_Package_One
from .forms import Data_Package_OneForm, Child_Package_OneForm

from destiny.models import Destiny



#===============================================================================
# DADOS PARA PACOTE - Data_package_One
# client => package

def data_package_list(request, id_destiny):
    destiny = Destiny.objects.filter(id=id_destiny).first()
    object = Data_Package_One.objects.filter(destiny_id=id_destiny)
    
    context = {
        'destiny': destiny,
        'object': object,
    }
    return render(request, 'package/data_package_list.html', context)

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


class DataPackageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Data_Package_One
    template_name = 'package/data_package_delete.html'
    success_message = 'Pacote deletado com sucesso!!!'

    def get_success_url(self):
        return reverse('package:data_package_list', kwargs={'id_destiny': self.object.destiny_id})

    def delete(self, request, *args, **kwargs):
        return super(DataPackageDeleteView, self).delete(request, *args, **kwargs)

data_package_delete = DataPackageDeleteView.as_view()


# def children_ages(request, id_package):
#     package = Data_Package_One.objects.filter(id=id_package)
#     object = Child_Package_One.objects.filter(Data_package_one=id_package)
#     context = {
#         'package': package,
#         'object': object,
#     }
#     return render(request, 'package/children_ages_list.html', context)


@login_required
def children_ages_update(request, id_package):
    
    package=Data_Package_One.objects.filter(id=id_package)
    Child_Age_formset = modelformset_factory(Child_Package_One, form=Child_Package_OneForm, extra=0)
    destiny_id=[]
    destiny=[]
    for p in package:
        destiny_id = p.destiny_id
        destiny = p.destiny
    
    if request.method == 'POST':
        formset = Child_Age_formset(request.POST, queryset=Child_Package_One.objects.filter(Data_package_one=id_package))

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            messages.success(request, 'Idade(s) alterada(s) com sucesso!!!')
            return redirect('package:data_package_list', id_destiny=destiny_id)

    formset = Child_Age_formset(queryset=Child_Package_One.objects.filter(Data_package_one=id_package))

    context = {
        'destiny': destiny,
        'package': package,
        'formset':formset,
    }
    return render(request, 'package/children_ages_update.html', context)

  