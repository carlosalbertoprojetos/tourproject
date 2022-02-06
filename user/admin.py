from django.contrib import admin

from .models import Contact, SocialMedia, User


class ContactAdmin(admin.TabularInline):
    model = Contact
    extra = 0


class SocialMediaAdmin(admin.TabularInline):
    model = SocialMedia
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'option', 'is_active')
    inlines = [
        ContactAdmin,
        SocialMediaAdmin,
    ]
    readonly_fields = ('option',)
    fields = ['option', ('email', 'username', 'is_active')]
