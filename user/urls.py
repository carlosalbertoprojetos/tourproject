from django.urls import path
from django.views.generic import TemplateView

# from .views import AgentCreatView


app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(template_name='user/dashboard.html'), name='dashboard'),
    # path('', AgentCreatView.as_view(), name='agent_signup'),
]
