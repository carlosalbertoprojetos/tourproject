from django.urls import path

from .views import client_list

app_name = 'client'

urlpatterns = [   
     
    path('list/', client_list,name='client_list'),
    
    #path('register/', RegisterClientView.as_view(), name='client_register'),

    #path('<int:pk>/edit/', UpdateClientView.as_view(), name='client_edit'),
]