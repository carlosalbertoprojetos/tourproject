
from django.contrib import admin

from .models import Trip, TripCategory, TripCategoryPax, TripOption, TripPrice


@admin.register(TripCategoryPax)
class TripCategoryPaxAdmin(admin.ModelAdmin):
    ...

@admin.register(TripCategory)
class TripCategoryAdmin(admin.ModelAdmin):
    model = TripCategory
    ordering = ('name',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    ...

@admin.register(TripOption)
class TripOptionAdmin(admin.ModelAdmin):
    ...


@admin.register(TripPrice)
class TripPriceAdmin(admin.ModelAdmin):
    ...
