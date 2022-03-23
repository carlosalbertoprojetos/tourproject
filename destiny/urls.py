from django.urls import path

from .views import (
    destiny_create, destinies_list, destiny_update, destiny_delete,
    destiny_period_season_create, destiny_period_seasons_list, destiny_period_season_update, destiny_period_season_delete,
)

app_name = 'destiny'

urlpatterns = [
    path('create/', destiny_create, name='destiny_create'),
    path('list/', destinies_list, name='destinies_list'),
    path('<int:pk>/edit/', destiny_update, name='destiny_update'),
    path('<int:pk>/delete/', destiny_delete, name='destiny_delete'),
    
    path('period/list/', destiny_period_seasons_list, name='destiny_period_seasons_list'),
    path('period/create/', destiny_period_season_create, name='destiny_period_season_create'),
    path('period/<int:pk>/edit/', destiny_period_season_update, name='destiny_period_season_update'),
    path('period/<int:pk>/delete/', destiny_period_season_delete, name='destiny_period_season_delete'),    
]