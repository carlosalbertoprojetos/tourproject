from django.contrib import admin

from .models import Company, CompanyDestinies


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'document_number', ]
    fields = [('responsible', 'company_name', 'document_number'),
              ('street', 'number', 'complement'), ('city', 'state', 'postal_code')]

@admin.register(CompanyDestinies)
class CompanyDestiniesAdmin(admin.ModelAdmin):
    ... 
    

