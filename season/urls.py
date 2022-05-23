from django.urls import path

from .views import (
   
    season_delete, season_list_create, season_update,
    validity_list_create, validity_delete,
    validity_update,event_list_create,event_delete,calendar_list
) 

app_name = 'season'

urlpatterns = [
    
    #EVENTO
    #path('event/list/', calendar_event, name='calendar_event'),
    path('event/list/', event_list_create, name='event_list_create'),
    path('<int:pk>/event/delete/', event_delete, name='event_delete'),
    path('calendar/list/', calendar_list, name='calendar_list'),       
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
    #path('period/list/', period_list_create, name='period_list_create'),
    #path('<int:pk>/option/edit/', period_update, name='period_update'),
    #path('<int:pk>/option/delete/', period_delete, name='period_delete'),
]
