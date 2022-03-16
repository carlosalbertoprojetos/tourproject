from django.urls import path

from .views import Client_list, Client_register, client_update 


app_name = 'client'

urlpatterns = [   
     
    path('list/', Client_list, name='client_list'),
    
    path('register/', Client_register, name='client_register'),      

    path('<int:id>/edit/', client_update, name='client_update'),
    
]