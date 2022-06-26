from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory, modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy as _
from django.views.generic.edit import DeleteView, UpdateView
from regex import F

from .models import Data_Package_One, Child_Package_One
from .forms import Data_Package_OneForm, Child_Package_OneForm

from destiny.models import Destiny



#===============================================================================
# DADOS PARA PACOTE - Data_package_One
# client => package


def data_package_create(request):
    # destiny = request.destiny
    Formset_Factory = inlineformset_factory(
    Data_Package_One, Child_Package_One, fields=('children_age',), extra=3, can_delete=False)

    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None)
        formset = Formset_Factory(request.POST or None)
        
        if form.is_valid() and formset.is_valid():
            package = form.save(commit=False)
            # package.destiny = destiny.id
            package.save()
            formset.instance = package
            formset.save()
            return redirect('package:data_package_create')
        else:
            context = {
                # 'destiny': destiny,
                'form': form,
                'formset': formset,
            }    
        return render(request, 'destiny/destiny_list_create.html', context)

    elif request.method == 'GET':
        form = Data_Package_OneForm()
        formset = Formset_Factory()
        
        context = {
            # 'destiny': destiny,
            'form': form,
            'formset': formset,
        }
        return render(request, 'package/data_package_create.html', context)


""" 
def data_package_create(request, id_destiny):
    destiny = Destiny.objects.get(id=id_destiny)
      
    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None)
        Formset_Factory = inlineformset_factory(Data_Package_One, Child_Package_One, form=Child_Package_OneForm)
        formset = Formset_Factory(request.POST or None)
        if all([form.is_valid(), formset.is_valid()]):
            package = form.save()
            formset.instance = package
            formset.save()
            return redirect('package:data_package_create', id_destiny)   

        else:
            context = {
                'form': form,
                'formset':formset,
                'destiny': destiny
                }
            return render(_('package:data_package_create', id_destiny))

    else:
        form = Data_Package_OneForm()
        Formset_Factory = inlineformset_factory(Data_Package_One, Child_Package_One, form=Child_Package_OneForm)
        formset = Formset_Factory()
        context = {
            'form': form,
            'formset':formset,
            'destiny': destiny
            }
        return redirect(_('destiny/destiny_list_create', context)) """
""" 
    if request.method == 'POST':
        form = Data_Package_OneForm(request.POST or None, instance=Data_Package_One)

        Formset_Factory = inlineformset_factory(Data_Package_One, Child_Package_One, form=Child_Package_OneForm, can_delete=False, extra=5)
        formset = Formset_Factory(request.POST or None)

        if all(form.is_valid(), formset.is_valid()):
            form = form.save(commit=False)
            form.destiny_id = destiny.id
            form.save()
            formset.instance = form
            formset.save()
            messages.success(request, 'Pacote cadastrado com sucesso!!!')
            return redirect('package:data_package_list')

        else:
            context = {
                'form': form,
                'formset' : formset,
                'destiny': destiny
            }
            return render(request, 'package/data_package_create.html', context)


    elif request.method == 'GET':
        form = Data_Package_OneForm(instance=Data_Package_One)

        Formset_Factory = inlineformset_factory(Data_Package_One, Child_Package_One, form=Child_Package_OneForm, can_delete=False, extra=0)        
        formset = Formset_Factory()

        context = {
                'form': form,
                'formset' : formset,
                'destiny': destiny
            }
        return render(request, 'package/data_package_create.html', context)
 """

def data_package_list(request, id_destiny):
    object = Data_Package_One.objects.filter(destiny_id=id_destiny)
    context = {
        'object': object,
    }
    return render(request, 'package/data_package_list.html', context)


class DataPackageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Data_Package_One
    form_class = Data_Package_OneForm
    template_name = 'package/data_package_update.html'
    # success_message = 'atualizada com sucesso!!!'
    success_url = _('package:data_package_list_create')

data_package_update = DataPackageUpdateView.as_view()


class DataPackageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Data_Package_One
    template_name = 'package/data_package_delete.html'
    # success_message = 'deletada com sucesso!!!'
    success_url = _('package:data_package_list_create')

    def delete(self, request, *args, **kwargs):
        return super(DataPackageDeleteView, self).delete(request, *args, **kwargs)

data_package_delete = DataPackageDeleteView.as_view()

