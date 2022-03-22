from django.urls import path

from .views import (season_create, seasons_list, season_update, season_delete,
                    period_season_create, period_seasons_list, period_season_update, period_season_delete
                    )

app_name = 'season'

urlpatterns = [   
    path('list/', seasons_list, name='seasons_list'),
    path('create/', season_create, name='season_create'),
    path('<int:pk>/edit/', season_update, name='season_update'),
    path('<int:pk>/delete/', season_delete, name='season_delete'),
    
    path('period/list/', period_seasons_list, name='period_seasons_list'),
    path('period/create/', period_season_create, name='period_season_create'),
    path('period/<int:pk>/edit/', period_season_update, name='period_season_update'),
    path('period/<int:pk>/delete/', period_season_delete, name='period_season_delete'),    
]