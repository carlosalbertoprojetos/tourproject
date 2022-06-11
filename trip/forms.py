from destiny.models import Destiny
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import (Activity, ActivityCatPax, ActivityPrice, CategoryPax,
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
    # activity = forms.CharField(label='',
    #     widget=forms.TextInput(
    #         attrs={'readonly': 'readonly'}
    #         )
    #     )
    # catpax = forms.CharField(label='',
    #     widget=forms.TextInput(
    #         attrs={'readonly': 'readonly'}
    #         )
    #     )
    # season = forms.CharField(label='',
    #     widget=forms.TextInput(
    #         attrs={
    #             'readonly': 'readonly',
    #             "class":'row col-md-4 text-center',
    #             }
    #         )
    #     )
    # price = forms.DecimalField(
    #     widget=forms.NumberInput(
    #         attrs={"class":'text-center',
    #             }
    #         )
    #     )
    class Meta:
        model = ActivityPrice
        # fields = '__all__'
        fields = ['activity', 'price',]
        widgets = {
            'activity':forms.TextInput({'class': 'row col-md-6 text-center', 'readonly':'readonly', 'type':'hidden'}),
            # 'activity':forms.TextInput({'class': 'row col-md-6 text-center', 'readonly':'readonly'}),
            # 'catpax':forms.TextInput({'class': 'row col-md-6 text-center', 'readonly':'readonly'}),
            # 'season':forms.TextInput({'class': 'row col-md-6 text-center', 'readonly':'readonly'}),
            'price':forms.NumberInput({'class':'form_control text-center mask-real'}),
            }
        labels = {"price":''}
