from django import forms

from .models import Transport, Transport_Type, TransportCategoryPax, TransportPrices


class TransportTypeForm(forms.ModelForm):

    class Meta:
        model = Transport_Type
        fields = '__all__'


class TransportCategoryPaxForm(forms.ModelForm):

    class Meta:
        model = TransportCategoryPax
        fields = '__all__'


class TransportForm(forms.ModelForm):

    class Meta:
        model = Transport
        fields = '__all__'


class TransportPriceForm(forms.ModelForm):

    class Meta:
        model = TransportPrices
        fields = '__all__'