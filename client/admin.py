from django.contrib import admin

# Register your models here.

from .models import Client


#class ContactAdmin(admin.TabularInline):
#    model = Client
#    extra = 0

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'cel', 'is_active')
    

admin.site.register(Client, ClientAdmin)    