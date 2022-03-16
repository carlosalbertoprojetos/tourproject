from django.contrib import admin

from .models import Company, Destiny, CompanyDestiny


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'document_number', ]
    fields = [('responsible', 'company_name', 'document_number'),
              ('street', 'number', 'complement'), ('city', 'state', 'postal_code')]


@admin.register(Destiny)
class DestinyAdmin(admin.ModelAdmin):
    ...
    
@admin.register(CompanyDestiny)
class CompanyDestinyAdmin(admin.ModelAdmin):
    ... 
