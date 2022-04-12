from django import forms

from .models import Destiny

class DestinyForm(forms.ModelForm):
 
    class Meta:
        model = Destiny
        fields = '__all__'