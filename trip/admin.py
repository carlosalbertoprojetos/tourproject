
from django.contrib import admin

from .models import TripCategory, Trip


@admin.register(TripCategory)
class TripCategoryAdmin(admin.ModelAdmin):
    model = TripCategory
    ordering = ('name',)


@admin.register(Trip)
class ProductsAdmin(admin.ModelAdmin):
    ...