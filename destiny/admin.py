from django.contrib import admin

from .models import Destiny


@admin.register(Destiny)
class DestinyAdmin(admin.ModelAdmin):
    ... 
