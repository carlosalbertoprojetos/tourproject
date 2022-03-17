from django.contrib import admin

from .models import Destiny

class DestinyAdmin(admin.ModelAdmin):
    list_display = ('season','destiny', 'state','city','date_start','date_finish', 'active', 'description')
    
admin.site.register(Destiny, DestinyAdmin)   
