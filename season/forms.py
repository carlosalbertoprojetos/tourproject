from django import forms
from .models import Season
 
 
# creating a form
class RegisterCalendarForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Season
 
        # specify fields to be used
        fields = '__all__'