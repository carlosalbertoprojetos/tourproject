from django.contrib import admin

from .models import Validity, OptionsPrices, PricesSeasonsDestinies


@admin.register(Validity)
class SeasonAdmin(admin.ModelAdmin):
    ...


@admin.register(OptionsPrices)
class OptionsPricesAdmin(admin.ModelAdmin):
    ...
    

@admin.register(PricesSeasonsDestinies)
class PricesSeasonsDestiniesAdmin(admin.ModelAdmin):
    ...