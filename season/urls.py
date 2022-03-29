from django.urls import path

from .views import (
    season_create, seasons_list, 
    season_update, season_delete,
    options_prices_create, options_prices_update,
    prices_season_list, prices_season_delete, 
    prices_season_create, 
    prices_season_update, prices_season_delete,
    )

app_name = 'season'

urlpatterns = [   
    path('list/', seasons_list, name='seasons_list'),
    path('create/', season_create, name='season_create'),
    path('<int:pk>/edit/', season_update, name='season_update'),
    path('<int:pk>/delete/', season_delete, name='season_delete'),

    path('prices/list/', prices_season_list, name='prices_season_list'),
    path('prices/create/', prices_season_create, name='prices_season_create'),
    path('<int:pk>/prices/edit/', prices_season_update, name='prices_season_update'),
    path('<int:pk>/prices/delete/', prices_season_delete, name='prices_season_delete'),

    path('option/create/', options_prices_create, name='options_prices_create'),
    path('<int:pk>/option/edit/', options_prices_update, name='options_prices_update'),
    path('<int:pk>/option/delete/', options_prices_update, name='options_prices_update'),

]