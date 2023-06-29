from django import forms
from django import forms
from django.contrib.admin.widgets import  AdminDateWidget
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Season, Validity, Event

class ValidityForm(forms.ModelForm):
    
    class Meta:
        model = Validity
        fields = '__all__' 
        
class SeasonForm(forms.ModelForm):

    class Meta:
        model = Season
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(name)s %(destiny)s %(validity)s já está cadastrado.",
            }
        }        


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"
        exclude = ('season',)
        widgets = {

            "date_init": AdminDateWidget(),
            "date_fin": AdminDateWidget(),  
        }
        
