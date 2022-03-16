from django.urls import path

from .views import Destiny_list, Destiny_register, Destiny_Delete, destiny_update

app_name = 'destino'

urlpatterns = [   
     
    path('list/', Destiny_list, name='destiny_list'),    
    
    path('register/', Destiny_register, name='destiny_register'),    

    path('<int:pk>/edit/', destiny_update, name='destiny_update'),

    path('<int:pk>/delete/', Destiny_Delete, name='destiny_delete'),    
    
]