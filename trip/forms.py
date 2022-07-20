from destiny.models import Destiny
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import (Activity, ActivityPrice, CategoryPax,
                     Trip, TripCategory, ActivityCatPax)


class TripCategoryForm(forms.ModelForm):
    
    class Meta:
        model = TripCategory
        fields = '__all__'


class TripForm(forms.ModelForm):
    destiny = forms.ModelChoiceField(queryset=Destiny.objects.all(), label='Destino')
    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['trip_duration'].widget.attrs.update(
            {'class': 'mask-hora'})
        self.fields['travel_time'].widget.attrs.update(
            {'class': 'mask-hora'})
        self.fields['travel_time_untoplace'].widget.attrs.update(
            {'class': 'mask-hora'})
        self.fields['commission'].widget.attrs.update(
            {'class': 'mask-perc'})


class CategoryPaxForm(forms.ModelForm):    
    class Meta:
        model = CategoryPax 
        fields = '__all__'
        # fields = ['name', 'note', 't_child', 'age_min', 'age_max']
        
        widgets = {
            't_adult':forms.CheckboxInput(attrs={'class':''}),
            't_child':forms.CheckboxInput(attrs={'class':''}),
            't_guest':forms.CheckboxInput(attrs={'class':''}),
            'age_min':forms.NumberInput(attrs={'class':'form-inline col-md-2 text-center'}),
            'age_max':forms.NumberInput(attrs={'class':'form-inline col-md-2 text-center'}),
            }


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = '__all__'
        exclude = ['trip',]

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['catpax'].widget = CheckboxSelectMultiple()
        self.fields['catpax'].queryset = CategoryPax.objects.all()


class ActivityPriceForm(forms.ModelForm):

    class Meta:
        model = ActivityPrice
        fields = ['activity', 'catpax', 'price',]
        widgets = {
            'activity':forms.TextInput({'readonly':'readonly', 'type':'hidden'}),
            'catpax':forms.TextInput({'readonly':'readonly', 'type':'hidden'}),
            'price':forms.NumberInput(attrs={'class':'text-center', 'style': 'border: 0; padding: 0 5px;',
            # 'data-inputmask':"'prefix': 'R$ ;'"
            }),
            }
        labels = {"price":''}



class CHD_ActivityForm(forms.ModelForm):
    
    class Meta:
        model = ActivityCatPax
        fields = '__all__'