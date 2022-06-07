from django.urls import path

from .views import (categorypax_list_create, categorypax_update, categorypax_delete, 
                    trip_category_list_create, trip_category_update, trip_category_delete,
                    
                    trip_list_create, trip_delete, trip_update,
                    
                    activity_list_create, activity_update, activity_delete, 
                    
                    activity_price_list_create, activity_price_update_tr, activity_price_update, activity_price_delete
                    )

app_name = 'trip'


urlpatterns = [    
    #=================================================================
    # CATEGORIA DE PASSEIO
    path('category/list/create/', trip_category_list_create, name="trip_category_list_create"), 
    path('<int:pk>/category/edit/', trip_category_update, name='trip_category_update'),
    path('<int:pk>/category/delete/', trip_category_delete, name='trip_category_delete'),
    
    #=================================================================
    # PASSEIO
    path('list/create/', trip_list_create, name='trip_list_create'),
    path('<int:pk>/edit/', trip_update, name='trip_update'),
    path('<int:pk>/delete/', trip_delete, name='trip_delete'),
    
    #=================================================================
    # CATEGORIA PAX
    path('categorypax/list/create/', categorypax_list_create, name='categorypax_list_create'),
    path('<int:pk>/categorypax/edit/', categorypax_update, name='categorypax_update'),
    path('<int:pk>/categorypax/delete/', categorypax_delete, name='categorypax_delete'),
    
    #=================================================================
    # ATIVIDADES
    path('<trip_id>/activity/list/create/', activity_list_create, name='activity_list_create'),
    path('<trip_id>/activity/edit/', activity_update, name='activity_update'),
    path('<int:pk>/activity/delete/', activity_delete, name='activity_delete'),

    #=================================================================
    # PREÇOS DAS ATIVIDADES
    path('<trip_id>/price_activity/list/create/', activity_price_list_create, name='activity_price_list_create'),
    path('<trip_id>/price_activity/edittr/', activity_price_update_tr, name='activity_price_update_tr'),
    path('<trip_id>/price_activity/edit/', activity_price_update, name='activity_price_update'),
    path('<int:pk>/price_activity/delete/', activity_price_delete, name='activity_price_delete'),
]
