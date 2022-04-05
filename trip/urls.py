from django.urls import path

from .views import (category_register, trip_create, trip_list, trip_update, trip_delete,
                    catpax_list, catpax_create, catpax_update, catpax_delete,
                    price_trip_list, price_trip_create, price_trip_update, price_trip_delete

                    )

app_name = 'trip'


urlpatterns = [
    path('category/', category_register, name="category_register"),

    #===============================================================
    #PASSEIO
    path('create/', trip_create, name='trip_create'),
    path('list/', trip_list, name='trip_list'),
    path('<int:pk>/edit/', trip_update, name='trip_update'),
    path('<int:pk>/delete/', trip_delete, name='trip_delete'),

    #===============================================================
    #PAX

    path('catpax/list/', catpax_list, name='catpax_list'),
    path('catpax/create/', catpax_create, name='catpax_create'),
    path('<int:pk>/catpax/edit/', catpax_update, name='catpax_update'),
    path('<int:pk>/catpax/delete/', catpax_delete, name='catpax_delete'),


    #===============================================================
    #PREÇÇO

    path('price_trip/list/', price_trip_list, name='price_trip_list'),
    path('price_trip/create/', price_trip_create, name='price_trip_create'),
    path('<int:pk>/price_trip/edit/', price_trip_update, name='price_trip_update'),
    path('<int:pk>/price_trip/delete/', price_trip_delete, name='price_trip_delete'),

]

