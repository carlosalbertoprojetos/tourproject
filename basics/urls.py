from django.urls import path

from .views import (categorypax_delete, categorypax_list_create,
                    categorypax_update)

app_name = 'basics'


urlpatterns = [
    path('categorypax/create/', categorypax_list_create, name='categorypax_list_create'),
    path('<int:pk>/categorypax/edit/', categorypax_update, name='categorypax_update'),
    path('<int:pk>/categorypax/delete/', categorypax_delete, name='categorypax_delete'),
]
