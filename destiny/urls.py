from django.urls import path

from .views import destiny_create, destinies_list, destiny_update

app_name = 'destiny'

urlpatterns = [
    path('create/', destiny_create, name='destiny_create'),
    path('list/', destinies_list, name='destinies_list'),
    path('<int:pk>/edit/', destiny_update, name='destiny_update'),
]
