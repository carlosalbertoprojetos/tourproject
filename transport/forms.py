from django import forms
from .models import Transport
 
 
# creating a form
class RegisterTransportForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Transport
 
        # specify fields to be used
        fields = '__all__'
    

class EditTransportForm(forms.ModelForm):

    class Meta:
        model = Transport
        fields = ['trecho','acessos'] 
