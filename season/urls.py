from django.urls import path

from .views import season_create, season_delete, season_update, seasons_list

app_name = 'season'

urlpatterns = [   
    path('list/', seasons_list, name='seasons_list'),
    path('create/', season_create, name='season_create'),
    path('<int:pk>/edit/', season_update, name='season_update'),
    path('<int:pk>/delete/', season_delete, name='season_delete'),    
]