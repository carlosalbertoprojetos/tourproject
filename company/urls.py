from django.urls import path

from .views import (companies_list, company_agents_list, company_update, company_delete,
                    signup_step_2)

app_name = 'company'

urlpatterns = [
    path('signup/2/', signup_step_2, name='signup2'),

    path('list/', companies_list, name='companies_list'),
    path('<int:pk>/update/', company_update, name='company_update'),
    path('<int:pk>/delete/', company_delete, name='company_delete'),
    
    path('agents/list/', company_agents_list, name='company_agents_list'),   
]
