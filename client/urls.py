from django.urls import path

from .views import Client_list, client_register, client_edit 


app_name = 'client'

urlpatterns = [   
     
    path('list/', Client_list, name='client_list'),
    
    path('register/', client_register, name='client_register'),    

    path('<int:pk>/edit/', client_edit, name='client_edit'),
    
]