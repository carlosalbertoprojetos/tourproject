from django.contrib import admin

# Register your models here.

from .models import Transport


class TransportAdmin(admin.ModelAdmin):
    list_display = ('id','trecho', 'acessos', 'is_active')
    

admin.site.register(Transport, TransportAdmin)   
