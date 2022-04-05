from django.contrib import admin

from .models import Destiny



class DestinyAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('name', 'state','city', 'active',)
    
admin.site.register(Destiny, DestinyAdmin)
=======
    list_display = ('name', 'city','state', 'is_active',)
    
admin.site.register(Destiny, DestinyAdmin)


>>>>>>> novo_transport
