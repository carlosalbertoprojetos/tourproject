from django.contrib import admin

from .models import Company, CompanyDestinies


# @admin.register(CompanyDestinies)
# class CompanyDestiniesAdmin(admin.TabularInline):
#     list_display = ['company', 'destiny']
#     model = CompanyDestinies
#     fields = ('destiny',)
#     ... 

# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ['company_name', 'document_number', ]
#     fields = [('responsible', 'company_name', 'document_number'),
#               ('street', 'number', 'complement'), ('city', 'state', 'postal_code')]
#     inlines = [
#         CompanyDestiniesAdmin,
#     ]
#     ...
    

