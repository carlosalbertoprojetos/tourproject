from django.contrib import admin

from .models import Destiny, DestinyPeriodSeasons



class DestinyAdmin(admin.ModelAdmin):
    list_display = ('name', 'state','city', 'active',)
    
admin.site.register(Destiny, DestinyAdmin)


@admin.register(DestinyPeriodSeasons)
class DestinyPeriodSeasonsAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'description', 'season', 'date_start', 'date_end')
    ...