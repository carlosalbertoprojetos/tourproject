from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'document_number', ]
    fields = [('company_name', 'document_number', 'document_image'),
              ('street', 'number', 'complement'), ('city', 'state', 'postal_code')]
