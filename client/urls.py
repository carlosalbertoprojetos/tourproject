from django.urls import path

from .views import client_delete, client_list_create, client_update

app_name = 'client'

urlpatterns = [
    path('list/', client_list_create, name='client_list_create'),    
    path('<int:pk>/edit/', client_update, name='client_update'),
    path('<int:pk>delete/', client_delete, name='client_delete'),
]