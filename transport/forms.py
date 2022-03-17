from django import forms

from .models import Transport


class RegisterTransportForm(forms.ModelForm):
 
    class Meta:
        model = Transport
        fields = '__all__'
    

class EditTransportForm(forms.ModelForm):

    class Meta:
        model = Transport
        fields = ['stretch','hits', 'is_active', 'document', 'description'] 
