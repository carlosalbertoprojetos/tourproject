from django.contrib import admin

# from .models import Package, Child_Package_One, PackageTrips



# class PackageTripsAdmin(admin.StackedInline):
#     model = PackageTrips
#     fields= ('id_price', 'package')
#     extra = 0
#     ...
    

# class Child_Package_OneAdmin(admin.StackedInline):
#     model = Child_Package_One
#     fields = ('children_age',)
#     extra = 0
#     ...


# @admin.register(Package)
# class PackageAdmin(admin.ModelAdmin):
#     list_display = ['destiny', 'date_arrive', 'date_departure']
#     readonly_fields= ('destiny',)
#     inlines = [
#         Child_Package_OneAdmin,
#         PackageTripsAdmin,
#     ]
#     ...
