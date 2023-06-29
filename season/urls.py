from django.urls import path

from .views import (
   
    season_delete, season_list_create, season_update,
    validity_list_create, validity_delete, validity_update,
    event_delete, calendar_event_detail, event_update_view,
    event_list, event_create_view
)

app_name = 'season'

urlpatterns = [
    path('<int:pk>/event/calendar/', calendar_event_detail, name='calendar_event_detail'),
    path('list/', season_list_create, name='season_list_create'),
    path('<int:pk>/update/', season_update, name='season_update'),
    path('<int:pk>/delete/', season_delete, name='season_delete'),
    path('validity/list/', validity_list_create, name='validity_list_create'),
    path('<int:pk>/validity/update/', validity_update, name='validity_update'),
    path('<int:pk>/validity/delete/', validity_delete, name='validity_delete'),
    path('<int:season_id>/event/', event_create_view, name='event_create'),
    path('<int:pk>/event/detail/', event_list, name='event_list'),
    path('<int:season_id>/event/<int:pk>/update/', event_update_view, name='event_update'),
    path('<int:season_id>/event/<int:pk>/delete/', event_delete, name='event_delete'), 
]
