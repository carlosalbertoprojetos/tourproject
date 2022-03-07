from django.urls import path

from .views import Transport_list, Transport_Delete, transport_register, transport_update

app_name = 'transport'

urlpatterns = [   
     
    path('list/', Transport_list, name='transport_list'),
    
    path('register/', transport_register, name='transport_register'),    

    path('<int:pk>/edit/', transport_update, name='transport_update'),

    path('<int:pk>/delete/', Transport_Delete, name='transport_delete'),    
    
]