from django.urls import path

from .views import (category_transport_list_create, 
                    category_transport_update, category_transport_delete,
                    catpax_transport_list_create, catpax_transport_delete, 
                    catpax_transport_update, price_transport_create,
                    price_transport_delete, price_transport_list_create,
                    price_transport_update, transport_delete,
                    transport_list_create, transport_update)

app_name = 'transport'

urlpatterns = [
    #=================================================================================
    # TRANSPORTE
    path('list/', transport_list_create, name='transport_list_create'), 
    path('<int:pk>/edit/', transport_update, name='transport_update'),
    path('<int:pk>/delete/', transport_delete, name='transport_delete'),
    
    #=================================================================================
    # CATEGORIA DE TRANSPORTE
    path('category/list/', category_transport_list_create, name='category_transport_list_create'),
    path('<int:pk>/category/edit/', category_transport_update, name='category_transport_update'),
    path('<int:pk>/category/delete/', category_transport_delete, name='category_transport_delete'),

    #=================================================================================
    # CATEGORIA PAX
    path('categorypax/list/', catpax_transport_list_create, name='catpax_transport_list_create'),
    
    path('<int:pk>/categorypax/edit/', catpax_transport_update, name='catpax_transport_update'),
    path('<int:pk>/categorypax/delete/',catpax_transport_delete, name='catpax_transport_delete'),

    #=================================================================================
    # PREÇOS TRANSPORTE
    path('price_transport/list/', price_transport_list_create, name='price_transport_list_create'),
    path('price_transport/create/', price_transport_create, name='price_transport_create'),
    path('<int:pk>/price_transport/edit/', price_transport_update, name='price_transport_update'),
    path('<int:pk>/price_transport/delete/', price_transport_delete, name='price_transport_delete'),
]   
    
