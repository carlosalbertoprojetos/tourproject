from django.urls import path

from .views import (transport_category_delete, transport_category_list_create,
                    transport_category_update, transport_catpax_delete,
                    transport_catpax_list_create, transport_catpax_update,
                    transport_delete, transport_list_create,
                    transport_price_delete, transport_price_list_create,
                    transport_price_update, transport_update)

app_name = 'transport'

urlpatterns = [
    #=================================================================================
    # CATEGORIA DE TRANSPORTE
    path('category/list/', transport_category_list_create, name='transport_category_list_create'),
    path('<int:pk>/category/edit/', transport_category_update, name='transport_category_update'),
    path('<int:pk>/category/delete/', transport_category_delete, name='transport_category_delete'),

    #=================================================================================
    # CATEGORIA PAX
    path('categorypax/list/', transport_catpax_list_create, name='transport_catpax_list_create'),
    path('<int:pk>/categorypax/edit/', transport_catpax_update, name='transport_catpax_update'),
    path('<int:pk>/categorypax/delete/',transport_catpax_delete, name='transport_catpax_delete'),
    
    #=================================================================================
    # TRANSPORTE
    path('list/', transport_list_create, name='transport_list_create'), 
    path('<int:pk>/edit/', transport_update, name='transport_update'),
    path('<int:pk>/delete/', transport_delete, name='transport_delete'),

    #=================================================================================
    # PREÇOS TRANSPORTE
    path('price_transport/list/', transport_price_list_create, name='transport_price_list_create'),
    path('<int:pk>/price_transport/edit/', transport_price_update, name='transport_price_update'),
    path('<int:pk>/price_transport/delete/', transport_price_delete, name='transport_price_delete'),
]