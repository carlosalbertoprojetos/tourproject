from django.urls import path
from django.views.generic import TemplateView

from .views import (edit_user_view, list_users)
from company.views import edit_company_view


app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='user/dashboard.html'), name='dashboard'),

    path('list/', list_users, name='list_users'),    
    path('<int:pk>/edit/', edit_user_view, name='edit_user'),
    
    path('<int:pk>/edit/company/', edit_company_view, name='edit_company'),
]

