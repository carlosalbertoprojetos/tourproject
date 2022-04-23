from django import forms
from .models import Trip, TripCategory, TripCategoryPax, TripOption, TripPrice
from .models import TripCategoryPax, TripCategory, Trip, TripPrice

class TripCategoryPaxForm(forms.ModelForm):
    
    class Meta:
        model = TripCategoryPax
        fields = '__all__'


class TripCategoryForm(forms.ModelForm):
    
    class Meta:
        model = TripCategory
        fields = '__all__'


class TripForm(forms.ModelForm):

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



class TripOptionsForm(forms.ModelForm):
    
    class Meta:
        model = TripOption
        fields = '__all__'


class TripPriceForm(forms.ModelForm):
    cadpax = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
            )
        )
    season = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={'readonly': 'readonly'}
            )
        )
    class Meta:
        model = TripPrice
        fields = ['cadpax', 'season', 'price',]
        widgets = {'price':forms.NumberInput({"class":'form_control text-center'}), }
        labels = {"cadapx":'', "season":'', "price":'',}
