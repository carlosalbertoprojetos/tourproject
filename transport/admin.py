from django.contrib import admin

# Register your models here.

from .models import Transport, Transport_Type, CategoriesPax, TransportPrices


class TransportAdmin(admin.ModelAdmin):
    list_display = ('stretch','hits', 'document', 'description', 'is_active')
    
admin.site.register(Transport, TransportAdmin)   

class Transport_TypeAdmin(admin.ModelAdmin):
    field = 'transport_type'
    
admin.site.register(Transport_Type, Transport_TypeAdmin) 

class CategoriesPaxAdmin(admin.ModelAdmin):
    list_display = ('transport_name', 'transport_type')
    
admin.site.register(CategoriesPax, CategoriesPaxAdmin) 

class TransportPricesAdmin(admin.ModelAdmin):
    list_display = ('transport', 'season', 'cadpax', 'price')
    
admin.site.register(TransportPrices, TransportPricesAdmin) 