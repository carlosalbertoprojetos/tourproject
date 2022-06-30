from django.contrib import admin

from .models import Data_Package_One, Child_Package_One

    
# @admin.register(Child_Package_One)
class Child_Packagen_OneAdmin(admin.StackedInline):
    list_display = ['children_age', ]
    model = Child_Package_One
    fields = ('children_age',)
    ...

@admin.register(Data_Package_One)
class Data_package_OneAdmin(admin.ModelAdmin):
    list_display = ['destiny', 'date_arrive', 'date_departure']
    inlines = [
        Child_Packagen_OneAdmin,
    ]
    ...
