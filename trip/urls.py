from django.urls import path

from .views import (trip_categorypax_list_create, trip_categorypax_update, trip_categorypax_delete,
                    trip_category_list_create, trip_category_update, trip_category_delete,
                    trip_list_create, trip_delete, trip_update,
                    trip_option_list_create, trip_option_update, trip_option_delete, 
                    trip_price_list_create, trip_price_update, trip_price_delete, trip_price_update_tr
                    )

app_name = 'trip'


urlpatterns = [
    #===============================================================================
    # CATEGORIA PAX DE PASSEIO
    path('categorypax/list/create/', trip_categorypax_list_create, name='trip_categorypax_list_create'),
    path('<int:pk>/categorypax/edit/', trip_categorypax_update, name='trip_categorypax_update'),
    path('<int:pk>/categorypax/delete/', trip_categorypax_delete, name='trip_categorypax_delete'),
    
    #===============================================================================
    # CATEGORIA DE PASSEIO
    path('category/list/create/', trip_category_list_create, name="trip_category_list_create"), 
    path('<int:pk>/category/edit/', trip_category_update, name='trip_category_update'),
    path('<int:pk>/category/delete/', trip_category_delete, name='trip_category_delete'),
    
    #===============================================================================
    # PASSEIO
    path('list/create/', trip_list_create, name='trip_list_create'),
    path('<int:pk>/edit/', trip_update, name='trip_update'),
    path('<int:pk>/delete/', trip_delete, name='trip_delete'),
    
    #===============================================================================
    # OPÇÕES DE PASSEIO
    path('<trip_id>/options/list/create/', trip_option_list_create, name='trip_option_list_create'),
    path('<int:pk>/option/edit/', trip_option_update, name='trip_option_update'),
    path('<int:pk>/option/delete/', trip_option_delete, name='trip_option_delete'),
    path('<int:pk>/delete/', trip_delete, name='trip_delete'),

    #===============================================================================
    # PREÇOS DOS PASSEIOS
    path('<trip_op_id>/price_trip/list/create/', trip_price_list_create, name='trip_price_list_create'),
    path('<trip_id>/price_trip/edit1/', trip_price_update_tr, name='trip_price_update_tr'),
    path('<trip_option_id>/price_op_trip/edit/', trip_price_update, name='tripop_price_update'),
    path('<int:pk>/price_trip/delete/', trip_price_delete, name='trip_price_delete'),
]
