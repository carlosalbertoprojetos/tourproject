from django import forms
from .models import Destiny
 
 
# creating a form
class RegisterDestinyForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Destiny
 
        # specify fields to be used
        fields = '__all__'
    

class EditDestinyForm(forms.ModelForm):

    class Meta:
        model = Destiny
        fields = '__all__' 
