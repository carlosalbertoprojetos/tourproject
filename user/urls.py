from django.urls import path
from django.views.generic import TemplateView

from .views import user_update, users_list, agent_signup

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='content_dashboard.html'), name='dashboard'),

    path('list/', users_list, name='users_list'),
    path('<int:pk>/edit/', user_update, name='user_update'),
    
    path('signup_agent/', agent_signup, name='agent_signup'),
]


        
