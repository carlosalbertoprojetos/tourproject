from django.urls import path
from django.views.generic import TemplateView

from .views import edit_user_admin, edit_user_view, list_users, signup_step_2, create_agent

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='user/dashboard.html'), name='dashboard'),
    
    path('signup/complement/', signup_step_2, name='signup_complement'),

    path('<int:pk>/edit/', edit_user_view, name='edit_user'),

    path('list/', list_users, name='list_users'),

    path('<int:pk>/editadmin/', edit_user_admin, name='edit_user_admin'),
    
    path('agent/', create_agent, name='create_agent')

]
