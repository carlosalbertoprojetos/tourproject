from django.urls import path
from django.views.generic import TemplateView

from .views import user_edit, users_list
from company.views import company_edit

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='content_dashboard.html'), name='dashboard'),

    path('list/', users_list, name='users_list'),
    path('<int:pk>/edit/', user_edit, name='user_edit'),
    
    # path('<int:pk>/edit/company/', company_edit, name='company_edit'),
]
