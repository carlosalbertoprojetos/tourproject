from django.urls import path

from .views import (price_trip_delete, price_trip_list_create,
                    price_trip_update, trip_category_delete,
                    trip_category_list_create, trip_category_update,
                    trip_delete, trip_list_create, trip_update)

app_name = 'trip'


urlpatterns = [
    #===============================================================================
    # CATEGORIA DE PASSEIO
    path('category/list/', trip_category_list_create, name="trip_category_list_create"), 
    path('<int:pk>/category/edit/', trip_category_update, name='trip_category_update'),
    path('<int:pk>/category/delete/', trip_category_delete, name='trip_category_delete'),
    
    #===============================================================================
    # PASSEIO
    path('list/', trip_list_create, name='trip_list_create'),
    path('<int:pk>/edit/', trip_update, name='trip_update'),
    path('<int:pk>/delete/', trip_delete, name='trip_delete'),

    #===============================================================================
    # PREÇOS DOS PASSEIOS
    path('price_trip/list/', price_trip_list_create, name='price_trip_list_create'),
    path('<int:pk>/price_trip/edit/', price_trip_update, name='price_trip_update'),
    path('<int:pk>/price_trip/delete/', price_trip_delete, name='price_trip_delete'),

]
