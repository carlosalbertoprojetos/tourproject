from django.contrib import admin

# Register your models here.

from .models import Destiny


class DestinyAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'state','description', 'is_active')
    

admin.site.register(Destiny, DestinyAdmin)   
