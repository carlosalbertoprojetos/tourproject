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
    #         'ride_distance',
    #         'limit_load',            
    #     ]}),
    #     ('Agência', {'fields': [
    #         'commission',
    #         'category',
    #         'company',
    #         'tour_notes',
    #         'featured_image',            
    #     ]}),
    # ]

    class Meta:
        model = Trip
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['trip_duration'].widget.attrs.update(
            {'class': 'mask-hora'})
        self.fields['travel_time'].widget.attrs.update(
            {'class': 'mask-hora'})
        self.fields['travel_time_untoplace'].widget.attrs.update(
            {'class': 'mask-hora'})
        self.fields['commission'].widget.attrs.update(
            {'class': 'mask-perc'})

        