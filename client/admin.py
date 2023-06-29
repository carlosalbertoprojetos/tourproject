from django.contrib import admin
from .models import Client



class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Cadastro', {
            'fields': ('name', 'cpf', 'email', 'phoneNumber', 'is_active')
        }),
        ('Endereço', {
            'classes': ('collapse',),
            'fields': ('street','number','complement','postal_code','state','city'),
        }),
    )
       

admin.site.register(Client, ClientAdmin)
