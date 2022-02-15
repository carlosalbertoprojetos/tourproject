from django.urls import path

from .views import companies_list, company_edit, signup_step_2

app_name = 'company'

urlpatterns = [
    path('signup/2/', signup_step_2, name='signup2'),

    path('list/', companies_list, name='companies_list'),
    path('<int:pk>/edit/', company_edit, name='company_edit'),
]
