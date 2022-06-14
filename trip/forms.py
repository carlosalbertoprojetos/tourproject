from destiny.models import Destiny
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import (Activity, ActivityPrice, CategoryPax,
                     Trip, TripCategory)


class TripCategoryForm(forms.ModelForm):
    
    class Meta:
        model = TripCategory
        fields = '__all__'


class TripForm(forms.ModelForm):
    destiny = forms.ModelChoiceField(queryset=Destiny.objects.all(), empty_label=None)
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


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['catpax'].widget = CheckboxSelectMultiple()
        self.fields['catpax'].queryset = CategoryPax.objects.all()


class ActivityPriceForm(forms.ModelForm):

    class Meta:
        model = ActivityPrice
        fields = ['activity', 'catpax', 'price',]
        widgets = {
            'activity':forms.TextInput({'class': 'row col-md-6 text-center', 'readonly':'readonly', 'type':'hidden'}),
            'catpax':forms.TextInput({'class': 'row col-md-6 text-center', 'readonly':'readonly', 'type':'hidden'}),
            'price':forms.NumberInput(attrs={'style': 'border: 0; padding:5px', 'class':'text-center'}),
            }
        labels = {"price":''}

