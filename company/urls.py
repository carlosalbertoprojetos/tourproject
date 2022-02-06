from django.urls import path
from django.views.generic import TemplateView

from .views import (edit_company_view, list_user_companies,
                    signup_step_2)


app_name = 'company'

urlpatterns = [
    path('signup/2/', signup_step_2, name='signup2'),
    
    path('list_companies/', list_user_companies, name='list_companies'),    

]

