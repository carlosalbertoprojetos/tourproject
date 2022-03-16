from django.contrib import admin

# Register your models here.

from .models import Client


#class ContactAdmin(admin.TabularInline):
#    model = Client
#    extra = 0

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf','street','number','complement','postal_code','state','city','email', 'phoneNumber', 'is_active')


admin.site.register(Client, ClientAdmin)    