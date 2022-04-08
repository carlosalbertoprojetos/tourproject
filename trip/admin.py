from django.contrib import admin

from .models import Categories, Trip


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    ordering = ('name',)


@admin.register(Trip)
class ProductsAdmin(admin.ModelAdmin):
    ...
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

