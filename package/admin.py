from django.contrib import admin

from .models import Data_Package_One, Child_Package_One


@admin.register(Data_Package_One)
class Data_package_OneAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Child_Package_One)
class Child_Packagen_OneAdmin(admin.ModelAdmin):
    ...
