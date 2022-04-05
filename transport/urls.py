from django.urls import path

from .views import (transport_list, transport_delete, transport_create, transport_update,
    category_transport_register, catpax_transport_list, catpax_transport_create, 
    catpax_transport_update, catpax_transport_delete, price_transport_list, 
    price_transport_create, price_transport_update, price_transport_delete
)

app_name = 'transport'

urlpatterns = [
     #=================================================================================
    #TRANSPORTE   
     
    path('list/', transport_list, name='transport_list'),    
    path('register/', transport_create, name='transport_create'), 
    path('<int:pk>/edit/', transport_update, name='transport_update'),
    path('<int:pk>/delete/', transport_delete, name='transport_delete'),    
    path('category/', category_transport_register, name="category_transport_register"),   

    #=================================================================================
    #PAX
    path('catpax/list/', catpax_transport_list, name='catpax_transport_list'),
    path('catpax/create/', catpax_transport_create, name='catpax_transport_create'),
    path('<int:pk>/catpax/edit/', catpax_transport_update, name='catpax_transport_update'),
    path('<int:pk>/catpax/delete/',catpax_transport_delete, name='catpax_transport_delete'),

    #=================================================================================
    #PREÇO
    path('price_transport/list/', price_transport_list, name='price_transport_list'),
    path('price_transport/reate/', price_transport_create, name='price_transport_create'),
    path('<int:pk>/price_transport/edit/', price_transport_update, name='price_transport_update'),
    path('<int:pk>/price_transport/delete/', price_transport_delete, name='price_transport_delete'),
]   
    
