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
    inlines = [
        ContactMixinAdmin,
        SocialMediaMixinAdmin
    ]
    ...
