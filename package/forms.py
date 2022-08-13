from django import forms
from django.forms import inlineformset_factory, modelformset_factory

from .models import Data_Package_One, Child_Package_One
# ,Data_Customer_Package
from django.contrib.admin.widgets import AdminDateWidget

class Data_Package_OneForm(forms.ModelForm):

    class Meta:
        model = Data_Package_One
        # fields = ['date_arrive', 'date_departure', 'num_adults', 'num_child']
        fields = '__all__'
        exclude = ['destiny']
        widgets = {
            'date_arrive':AdminDateWidget(
                attrs={'class': 'vDateField form-control mt-2', 
                        'title':"Selecione uma data",
                        'required': 'true',
                }
            ),
            'date_departure':AdminDateWidget(
                attrs={'class': 'vDateField form-control mt-2', 
                        'title':"Selecione uma data", 
                        'required': 'true',
                }
            ),           
            'num_adults':forms.NumberInput(
                attrs={
                    'class':'form-control mt-2',
                    'type':'number',
                    'required': 'true'
                    },
                ),                        
            'num_child':forms.NumberInput(
                attrs={
                    'class':'form-control mt-2',
                    'type':'number',
                    'required': 'true'
                    },
                ),
        }
class Child_Package_OneForm(forms.ModelForm):

    class Meta:
        model = Child_Package_One
        fields = ('children_age',)
        labels = {"Data_package_one":''}
        widgets = {
            'children_age':forms.NumberInput(
                attrs={
                    'class':'form-control mx-1 text-center',
                    'size': '2',
                    'type':'text',
                    # 'required': 'true' - não salva
                    },
                ),
            }


# class Data_Customer_PackageForm(forms.ModelForm):

#     class Meta:
#         model = Data_Customer_Package
#         fields = ('name', 'email', 'phonenumber', 'city', 'description')
#         widgets = {
#             'name':forms.TextInput(
#                 attrs={
#                     'class':'col-md-12 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true'
#                     },
#                 ),
#             'email':forms.TextInput(
#                 attrs={
#                     'class':'col-md-6 form-control mx-1 text-center',
#                     'type':'email',
#                     'required': 'true'
#                     },
#                 ),
#             'phonenumber':forms.TextInput(
#                 attrs={
#                     'class':'col-md-6 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true',
#                     'data-inputmask-mask':'"(9-)AAAAA-9999"',
#                     },
#                 ),
#             'city':forms.TextInput(
#                 attrs={
#                     'class':'col-md-12 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true'
#                     },
#                 ),
#             'description':forms.TextInput(
#                 attrs={
#                     'class':'col-md-12 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true'
#                     },
#                 ),
#             }

Formset_Factory = inlineformset_factory(
    Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)

Child_Age_formset = modelformset_factory(
    Child_Package_One, form=Child_Package_OneForm, extra=0)

Child_Formset_Factory = inlineformset_factory(
    Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)

Chosen_Formset_Factory = inlineformset_factory(
    Data_Package_One, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)