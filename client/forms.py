from django import forms
from .models import Client
 
 
# creating a form
class RegisterClientForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Client
 
        # specify fields to be used
        fields = '__all__'
    

class EditClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
