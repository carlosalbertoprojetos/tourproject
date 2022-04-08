from django import forms


from .models import Period, Season, Validity


class ValidityForm(forms.ModelForm):
    
    class Meta:
        model = Validity
        fields = '__all__'        


class PeriodForm(forms.ModelForm):
    
    class Meta:
        model = Period
        fields = '__all__'

class SeasonForm(forms.ModelForm):

    class Meta:
        model = Season
        fields = '__all__'        

