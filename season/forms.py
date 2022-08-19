from django import forms
#from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from django.contrib.postgres.forms.ranges import DateRangeField,RangeWidget
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Season, Validity, Event, Destiny

class ValidityForm(forms.ModelForm):    

    #year = forms.CharField(label='Ano',max_length=200)    
    #active = forms.BooleanField(label='Ativo Agência')
    #sell = forms.BooleanField(label='Ativo Venda')
    
    class Meta:
        model = Validity
        fields = '__all__' 
        
class SeasonForm(forms.ModelForm):

    #name = forms.CharField(label='Nome',max_length=255)
    #destiny = forms.ModelChoiceField(label='Destino', queryset = Destiny.objects.all())
    #validity = forms.ModelChoiceField(label='vigência',queryset = Validity.objects.all())
    #active_company = forms.BooleanField(label='Ativo Agência')
    #active_sell = forms.BooleanField(label='Ativo Venda')

    class Meta:
        model = Season
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(name)s %(destiny)s %(validity)s já está cadastrado.",
            }
        }        


class EventForm(forms.ModelForm):

    #date_init = DateRangeField(widget=RangeWidget(AdminDateWidget()))    

    class Meta:
        model = Event
        fields = "__all__"
        exclude = ('season',)
        widgets = {

            "date_init": AdminDateWidget(),
            "date_fin": AdminDateWidget(),
            #"season": forms.HiddenInput(),            
        }
        
        
'''
class DTForm(forms.Form):                 
    name_event = forms.CharField(label='Evento',max_length=255)
    date_init = forms.DateField(label='Data Inicial',widget=AdminDateWidget())
    date_fin = forms.DateField(label='Data Final',widget=AdminDateWidget())
    season = forms.ModelChoiceField(label='Temporada',queryset = Season.objects.all())
    #season = forms.ModelChoiceField(queryset = Season.objects.filter(season.name) )    
    

class DTModelForm(forms.ModelForm):
    date_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
            "time": AdminTimeWidget(),
        }
'''                     