from dataclasses import fields
from datetime import date
from pyexpat import model
from django import forms
from .models import Season, Validity,Event

class DateInput(forms.DateInput):
    input_type = 'date'
'''
class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)

class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'my_date_field' : DateInput()}
'''
class CommentForm(forms.Form):
    name = forms.CharField(label='Nome')
    url = forms.URLField()
    comment = forms.CharField(label='Comentário')
    data = forms.DateField(widget=DateInput)

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
                     

