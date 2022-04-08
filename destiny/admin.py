from django.contrib import admin

from .models import Destiny

class DestinyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'active',)
    
admin.site.register(Destiny, DestinyAdmin)
