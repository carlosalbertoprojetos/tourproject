from django.urls import path

from .views import Client_list, Client_create, client_register, client_edit 


app_name = 'client'

urlpatterns = [   
     
    path('list/', Client_list, name='client_list'),
    
    path('create/', Client_create, name='client_create'),
    
    path('register/', client_register, name='client_register'),    

    path('<int:id>/edit/', client_edit, name='client_edit'),
    
]