from django.contrib import admin

from .models import Company, CompanyDestinies, State, City


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'document_number', ]
    fields = [('responsible', 'company_name', 'document_number'),
              ('street', 'number', 'complement'), ('city', 'state', 'postal_code')]

    
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    ... 


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ... 


@admin.register(CompanyDestinies)
class CompanyDestiniesAdmin(admin.ModelAdmin):
    ... 
    

