from django import forms

from destiny.models import Destiny
from .models import Trip, TripCategory, TripCategoryPax, TripOption, TripPrice


class TripCategoryPaxForm(forms.ModelForm):
    
    class Meta:
        model = TripCategoryPax
        fields = '__all__'


class TripCategoryForm(forms.ModelForm):
    
    class Meta:
        model = TripCategory
        fields = '__all__'


from django.forms.widgets import CheckboxSelectMultiple

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
        self.fields['cadpax'].widget = CheckboxSelectMultiple()
        self.fields['cadpax'].queryset = TripCategoryPax.objects.all()

# class TripCategoriesCadPAXForm(forms.ModelForm):

#     class Meta:
#         model = TripCategoriesCadPAX
#         fields = '__all__'

class TripOptionsForm(forms.ModelForm):

    class Meta:
        model = TripOption
        fields = '__all__'


class TripPriceForm(forms.ModelForm):
    # cadpax = forms.CharField(label='',
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
        model = TripPrice
        fields = ['price',]
        # widgets = {
        # #     # forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
        # #     # 'season':forms.CharField({"class":'row col-md-6 text-center'}),
        #     'price':forms.NumberInput({"class":'form_control text-center mask-real'}),
        #     }
        labels = {"price":'',}


    def __init__(self, *args, **kwargs):
        super(TripPriceForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update(
            {'class': 'mask-real text-center  p-1'})
