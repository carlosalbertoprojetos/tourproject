from django.urls import path

from .views import (data_package_list,
                    data_package_create,
                    data_package_delete,
                    
                    children_ages_update,
                    )

app_name = 'package'


urlpatterns = [
    #=================================================================
    # PACOTES
    path('<id_destiny>/create/', data_package_create, name="data_package_create"),
    path('<id_destiny>/list/', data_package_list, name="data_package_list"),

    path('<int:pk>/delete/', data_package_delete, name='data_package_delete'),
    
    path('<id_package>/children_ages_update/', children_ages_update, name='children_ages_update')
]