from django.urls import path

from .views import (
    period_list_create, period_delete, period_update,
    season_delete, season_list_create, season_update,
    validity_list_create, validity_delete,
    validity_update,calendar_create,calendar_delete,calendar_event,calendar_list
) 

app_name = 'season'

urlpatterns = [
    
    #CALENDÁRIO
    path('calendar/', calendar_event, name='calendar_event'),
    path('calendar/create/', calendar_create, name='calendar_create'),
    path('calendar/list/', calendar_list, name='calendar_list'),    
    path('<int:pk>/calendar/delete/', calendar_delete, name='calendar_delete'),   
    #============================================================================
    #TEMPORADA
    path('list/', season_list_create, name='season_list_create'),
    path('<int:pk>/edit/', season_update, name='season_update'),
    path('<int:pk>/delete/', season_delete, name='season_delete'),    

    #============================================================================
    #VIGÊNCIA
    path('validity/list/', validity_list_create, name='validity_list_create'),
    path('<int:pk>/validity/edit/', validity_update, name='validity_update'),
    path('<int:pk>/validity/delete/', validity_delete, name='validity_delete'),

    #============================================================================
    #PERIODO
    path('period/list/', period_list_create, name='period_list_create'),
    path('<int:pk>/option/edit/', period_update, name='period_update'),
    path('<int:pk>/option/delete/', period_delete, name='period_delete'),
]
