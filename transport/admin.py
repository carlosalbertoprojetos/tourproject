from django.contrib import admin

from .models import Transport, Transport_Type, TransportCategoryPax, TransportPrices

class TransportAdmin(admin.ModelAdmin):
    list_display = ('stretch','hits', 'document', 'description', 'is_active')
    
admin.site.register(Transport, TransportAdmin)   

class Transport_TypeAdmin(admin.ModelAdmin):
    field = 'transport_type'
    
admin.site.register(Transport_Type, Transport_TypeAdmin) 

class CategoriesPaxAdmin(admin.ModelAdmin):
    list_display = ('transport_name', 'transport_type')
    
admin.site.register(TransportCategoryPax, CategoriesPaxAdmin) 

class TransportPricesAdmin(admin.ModelAdmin):
    list_display = ('transport', 'season', 'cadpax', 'price')
    
admin.site.register(TransportPrices, TransportPricesAdmin) 