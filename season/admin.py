from django.contrib import admin

from .models import Validity, Period, Season


@admin.register(Validity)
class SeasonAdmin(admin.ModelAdmin):
    ...


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    ...
    

@admin.register(Period)
class PeriodSeasonsDestiniesAdmin(admin.ModelAdmin):
    ...