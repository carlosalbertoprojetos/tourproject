from django.urls import path

from .views import (companies_list, company_update, signup_step_2, company_agents_list, destiny_create, destiny_list, destiny_update)

app_name = 'company'

urlpatterns = [
    path('signup/2/', signup_step_2, name='signup2'),

    path('list/', companies_list, name='companies_list'),
    path('<int:pk>/edit/', company_update, name='company_update'),
    
    path('agents/list/', company_agents_list, name='company_agents_list'),
    
    path('create/destiny/', destiny_create, name='destiny_create'),
    path('list/destinies/', destiny_list, name='destiny_list'),
    path('<int:pk>/edit/destiny/', destiny_update, name='destiny_update'),
    
]
