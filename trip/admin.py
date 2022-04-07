from django.contrib import admin

from .models import Categories, Trip, CategoriesPax, TripSeasonPrices


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    ordering = ('name',)


@admin.register(Trip)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoriesPax)
class CategoriesPaxAdmin(admin.ModelAdmin):
    pass

@admin.register(TripSeasonPrices)
class TripSeasonPricesAdmin(admin.ModelAdmin):
    pass