from django import forms

from .models import CategoriesPax, Transport_Type, Transport


class CatPaxTransportForm(forms.ModelForm):
 
    class Meta:
        model = CategoriesPax
        fields = '__all__'


class TransportTypeForm(forms.ModelForm):
     
    class Meta:
        model = Transport_Type
        fields = '__all__'


class TransportForm(forms.ModelForm):
     
    class Meta:
        model = Transport
        fields = '__all__'
