from django import forms
from .models import Season, Validity,Event

class ValidityForm(forms.ModelForm):
    
    class Meta:
        model = Validity
        fields = '__all__' 
        
class SeasonForm(forms.ModelForm):

    class Meta:
        model = Season
        fields = '__all__'        

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"      
                     