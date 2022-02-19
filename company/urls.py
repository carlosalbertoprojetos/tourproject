from django.urls import path

from .views import companies_list, company_edit, signup_step_2, company_agents_list

app_name = 'company'

urlpatterns = [
    path('signup/2/', signup_step_2, name='signup2'),

    path('list/', companies_list, name='companies_list'),
    path('<int:pk>/edit/', company_edit, name='company_edit'),
    
    path('agents/list/', company_agents_list, name='company_agents_list'),
]
