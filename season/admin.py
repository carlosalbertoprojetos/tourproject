from django.contrib import admin

from .models import Validity, Period, Season, Event


@admin.register(Validity)
class SeasonAdmin(admin.ModelAdmin):
    pass    
    
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass

@admin.register(Period)
class PeriodSeasonsDestiniesAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

