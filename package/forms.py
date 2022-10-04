from django import forms
from django.forms import inlineformset_factory
from django.contrib.admin.widgets import AdminDateWidget

from .models import Package, Child_Package_One, PackageTrips

class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
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
            'name':forms.TextInput(
                attrs={
                    'class':'form-control mt-2',
                    'type':'text',
                    'required': 'true'
                    },
                ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control mt-2',
                    'type':'email',
                    'required': 'true'
                    },
                ),
            'phonenumber':forms.TextInput(
                attrs={
                    'class':'mask-telefone form-control mt-2',
                    'type':'text',
                    'required': 'true',
                    'max':"15"
                    },
                ),
            'city':forms.TextInput(
                attrs={
                    'class':'form-control mt-2',
                    'type':'text',
                    'required': 'true'
                    },
                ),
            'description':forms.Textarea(
                attrs={
                    'class':'form-control mt-2',
                    'type':'text',
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
                    },
                ),
            }


class Package_Trips_Form(forms.ModelForm):

    class Meta:
        model = PackageTrips
        fields = '__all__'
        labels = {"id_price":''}

ChildAge_Factory = inlineformset_factory(
    Package, Child_Package_One, form=Child_Package_OneForm, extra=0, can_delete=False)

PackageTrip_Factory = inlineformset_factory(
    Package, PackageTrips, form=Package_Trips_Form, extra=0, can_delete=False)