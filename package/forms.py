from django import forms
# from django.forms import inlineformset_factory, modelformset_factory

from .models import Data_Package_One, Child_Package_One


class Data_Package_OneForm(forms.ModelForm):
    
    class Meta:
        model = Data_Package_One
        fields = '__all__'
        # fields = ['date_arrive', 'date_departure', 'num_adults', 'num_child']
        widgets = {
            'date_arrive':forms.DateInput(attrs={'type':'date'}, ),
            'date_departure':forms.DateInput(attrs={'type':'date'}, ),
            'num_child':forms.NumberInput(attrs={'oninput':'campos()'}, ),
        }


class Child_Package_OneForm(forms.ModelForm):

    class Meta:
        model = Child_Package_One
        fields = '__all__'
        labels = {"Data_package_one":''}
        widgets = {}


        