from django import forms


from .models import PricesSeasonsDestinies


class PricesCreateForm(forms.ModelForm):
    class Meta:
        model = PricesSeasonsDestinies
        fields = '__all__'

      