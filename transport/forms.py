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
        widgets = {
            "transport_type": forms.Select(attrs={"class": "form-select"}),
            }

class TransportForm(forms.ModelForm):    

    class Meta:
        model = Transport
        fields = '__all__'
        widgets = {
            "destiny": forms.Select(attrs={"class": "form-select"}),
            "document": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            }

class TransportPriceForm(forms.ModelForm):

    class Meta:
        model = TransportPrices
        fields = '__all__'
        widgets = {
            "transport": forms.Select(attrs={"class": "form-select"}),
            "season": forms.Select(attrs={"class": "form-select"}),
            "cadpax": forms.Select(attrs={"class": "form-select"}),
            }