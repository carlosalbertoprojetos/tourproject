from django.contrib import admin

from .models import User

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     ...


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'option', ]

    fieldsets = [
        ('Usuário', {'fields': [('option', 'email'), 'document_number']}),
        ('Endereço', {'fields': [('street', 'number', 'complement', 'city')]}),
    ]


admin.site.register(User, UserAdmin)
