from django.urls import path

from .views import (companies_list, company_edit, company_edit_admin,
                    signup_step_2)

app_name = 'company'

urlpatterns = [
    path('signup/2/', signup_step_2, name='signup2'),

    path('list/companies/', companies_list, name='companies_list'),
    path('<int:pk>/edit/company/', company_edit, name='company_edit'),

    path('<int:pk>/admin/edit/company/',
         company_edit_admin, name='admin_company_edit'),
]
