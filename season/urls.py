from django.urls import path

from .views import (    
    season_create, seasons_list, season_update, season_delete, validity_list, 
    validity_create, validity_update, validity_delete, period_list, 
    period_create, period_update, period_delete

    )

app_name = 'season'

urlpatterns = [   
    #============================================================================
    #TEMPORADA

    path('list/', seasons_list, name='seasons_list'),
    path('create/', season_create, name='season_create'),
    path('<int:pk>/edit/', season_update, name='season_update'),
    path('<int:pk>/delete/', season_delete, name='season_delete'),    

    #============================================================================
    #VIGÊNCIA

    path('validity/list/', validity_list, name='validity_list'),
    path('validity/create/', validity_create, name='validity_create'),
    path('<int:pk>/validity/edit/', validity_update, name='validity_update'),
    path('<int:pk>/validity/delete/', validity_delete, name='validity_delete'),

    #============================================================================
    #PERIODO

    path('period/list/', period_list, name='period_list'),
    path('period/create/', period_create, name='period_create'),
    path('<int:pk>/option/edit/', period_update, name='period_update'),
    path('<int:pk>/option/delete/', period_delete, name='period_delete'),
]