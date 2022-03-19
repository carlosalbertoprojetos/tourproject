from django.urls import path

from .views import Calendar_register

app_name = 'season'

urlpatterns = [           
    
    path('register/', Calendar_register, name='calendar_register'),       
    
]