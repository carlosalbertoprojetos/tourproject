from django import forms

from .models import Data_Package_One, Child_Package_One


class Data_Package_OneForm(forms.ModelForm):
    
    class Meta:
        model = Data_Package_One
        # fields = '__all__'
        fields = ['date_arrive', 'date_departure', 'num_adults', 'num_child']
        # labels = {'date_arrive':'Data de chegada', 'date_departure':'Data de partida', 'num_adults':'Quantidade de adultos', 'num_child':'Quantidade de Crianças'}
        widgets = {
            'date_arrive':forms.DateInput(
                attrs={
                    'class':'form-control my-2',
                    # 'label':'Data de Chegada',
                    'type':'date'
                    },
                ),
            'date_departure':forms.DateInput(
                attrs={
                    'class':'form-control my-2',
                    # 'label':'Data de Partida',
                    'type':'date'
                    },
                ),
            
            'num_adults':forms.NumberInput(
                attrs={
                    'class':'form-control my-2',
                    # 'label':'Quantidade de Adultos',
                    'type':'number'
                    },
                ),
                        
            'num_child':forms.NumberInput(
                attrs={
                    'class':'form-control my-2',
                    # 'label':'Quantidade de Crianças',
                    'type':'number'
                    },
                ),
        }


class Child_Package_OneForm(forms.ModelForm):

    class Meta:
        model = Child_Package_One
        fields = ('children_age',)
        labels = {"Data_package_one":''}
        widgets = {
            'children_age':forms.TimeInput(
                attrs={
                    'class':'form-control m-1',
                    'type':'text'
                    },
                ),
        }
       