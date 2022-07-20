from django.contrib import admin

from .models import Data_Package_One, Child_Package_One
# Data_Customer_Package

    
# @admin.register(Child_Package_One)
class Child_Package_OneAdmin(admin.StackedInline):
    model = Child_Package_One
    fields = ('children_age',)
    ...

# class Data_Customer_PackageAdmin(admin.StackedInline):
#     model = Data_Customer_Package
#     fields = ('name', 'phonenumber', 'city')
#     ...

@admin.register(Data_Package_One)
class Data_package_OneAdmin(admin.ModelAdmin):
    list_display = ['destiny', 'date_arrive', 'date_departure']
    inlines = [
        Child_Package_OneAdmin,
        # Data_Customer_PackageAdmin,
    ]
    ...
