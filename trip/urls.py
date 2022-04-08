from django.urls import path

from .views import (price_trip_create, price_trip_delete, price_trip_list,
                    price_trip_update, trip_category_delete,
                    trip_category_update, trip_create, trip_delete, trip_list,
                    trip_list_category_create, trip_update)

app_name = 'trip'


urlpatterns = [

    path('category/create/', trip_list_category_create, name="trip_list_category_create"), 
    path('<int:pk>/category/edit/', trip_category_update, name='trip_category_update'),
    path('<int:pk>/category/delete/', trip_category_delete, name='trip_category_delete'),
    
    path('create/', trip_create, name='trip_create'),
    path('list/', trip_list, name='trip_list'),
    path('<int:pk>/edit/', trip_update, name='trip_update'),
    path('<int:pk>/delete/', trip_delete, name='trip_delete'),

    path('price_trip/list/', price_trip_list, name='price_trip_list'),
    path('price_trip/create/', price_trip_create, name='price_trip_create'),
    path('<int:pk>/price_trip/edit/', price_trip_update, name='price_trip_update'),
    path('<int:pk>/price_trip/delete/', price_trip_delete, name='price_trip_delete'),

]