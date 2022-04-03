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


    # list_display = ['category', 'name','price','available','description']
    # list_filter = ['category', 'name', 'available', 'created_at']
    # search_fields = ('category', 'name', 'available')
    # fieldsets = [
    #     ('Produto', {
    #         'fields': (('category', 'name'), ('price', 'available')),
    #     }),
    #     ('Detalhes', {
    #         'fields': ('description',)
    #     }),
    # ]
    # ordering = ('name',)

