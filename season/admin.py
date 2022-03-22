from django.contrib import admin

from .models import PeriodSeasons, Season


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    ...


@admin.register(PeriodSeasons)
class PeriodSeasonsAdmin(admin.ModelAdmin):
    list_display = ('description', 'season', 'date_start', 'date_end')
    ...
