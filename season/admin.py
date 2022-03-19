from django.contrib import admin

# Register your models here.

from .models import Season


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season', 'date_init','date_final', 'description')
    

admin.site.register(Season, SeasonAdmin) 