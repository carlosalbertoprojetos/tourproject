from django.urls import path

from .views import (
    destiny_create, destinies_list, destiny_update, destiny_delete,
    destiny_create_season, destinies_list_season,
    )

app_name = 'destiny'

urlpatterns = [
    path('create/', destiny_create, name='destiny_create'),
    path('list/', destinies_list, name='destinies_list'),
    path('<int:pk>/edit/', destiny_update, name='destiny_update'),
    path('<int:pk>/delete/', destiny_delete, name='destiny_delete'),
    
    path('create/season/', destiny_create_season, name='destiny_create_season'),
    path('list/season/', destinies_list_season, name='destinies_list_season'),
]

