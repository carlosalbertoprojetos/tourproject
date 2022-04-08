from django import forms

from .models import Trip


class TripForm(forms.ModelForm):
    # fieldsets = [
    #     ('Passeio', {'fields': [
    #         ('name', 'slug', 'image'),
    #     ]}),
    #     ('Detalhes', {'fields': [
    #         ('trip_description', 'short_description'),
    #         'politic', 
    #     ]}),
        
    #     ('Percurso', {'fields': [
    #         'trip_duration',
    #         'travel_time',
    #         'travel_time_untoplace',
    #         'limit_load',
    #     ]}),
    # ]

    class Meta:
        model = Trip
        fields = '__all__'

