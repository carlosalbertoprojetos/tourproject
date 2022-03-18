from django.contrib import admin

from .models import Destiny

class DestinyAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'state','city', 'active',)
    
admin.site.register(Destiny, DestinyAdmin)   
