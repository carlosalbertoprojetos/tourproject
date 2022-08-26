from django.contrib import admin

from .models import Data_Package_One, Child_Package_One, PackageTrips



class PackageTripsAdmin(admin.StackedInline):
    model = PackageTrips
    fields= ('id_price', 'package')
    extra = 0
    ...
    
# @admin.register(Child_Package_One)
class Child_Package_OneAdmin(admin.StackedInline):
    model = Child_Package_One
    fields = ('children_age',)
    extra = 0
    ...


@admin.register(Data_Package_One)
class Data_package_OneAdmin(admin.ModelAdmin):
    list_display = ['destiny', 'date_arrive', 'date_departure']
    readonly_fields= ('destiny',)
    inlines = [
        Child_Package_OneAdmin,
        PackageTripsAdmin,
    ]
    ...
