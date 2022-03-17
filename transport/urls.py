from django.urls import path

from .views import transport_list, transport_delete, transport_create, transport_update

app_name = 'transport'

urlpatterns = [   
     
    path('list/', transport_list, name='transport_list'),
    
    path('register/', transport_create, name='transport_create'),    

    path('<int:pk>/edit/', transport_update, name='transport_update'),

    path('<int:pk>/delete/', transport_delete, name='transport_delete'),    
    
]