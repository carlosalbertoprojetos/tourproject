from django import forms

from .models import Data_Package_One, Child_Package_One


class Data_Package_OneForm(forms.ModelForm):


    class Meta:
        model = Data_Package_One
        fields = ['date_arrive', 'date_departure', 'num_adults', 'num_child']
        widgets = {
            'date_arrive':forms.DateInput(
                attrs={
                    'class':'my-1',
                    'type':'date',
                    'required': 'true'
                    },
                ),
            'date_departure':forms.DateInput(
                attrs={
                    'class':'my-1',
                    'type':'date',
                    'required': 'true'
                    },
                ),            
            'num_adults':forms.NumberInput(
                attrs={
                    'class':'my-1',
                    'type':'number',
                    'required': 'true'
                    },
                ),                        
            'num_child':forms.NumberInput(
                attrs={
                    'class':'my-1',
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