from django.contrib import admin

from .models import ContactMixin, SocialMediaMixin, User


class ContactMixinAdmin(admin.TabularInline):
    model = ContactMixin
    extra = 1


class SocialMediaMixinAdmin(admin.TabularInline):
    model = SocialMediaMixin
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'option', 'is_active', 'document_number')
    inlines = [
        ContactMixinAdmin,
        SocialMediaMixinAdmin,
    ]
    readonly_fields = ('option',)
    fields = ['option', ('is_active', 'username', 'email'), 'groups', ('document_number', 'document_image'), 
              ('postal_code', 'street', 'number', 'complement', 'state')
              ]
    
