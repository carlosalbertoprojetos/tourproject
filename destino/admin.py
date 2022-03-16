from django.contrib import admin

# Register your models here.

from .models import Destiny


class DestinyAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'name','state','date_init','date_final','description', 'is_active')
    

admin.site.register(Destiny, DestinyAdmin)   
