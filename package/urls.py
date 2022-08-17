from django.urls import path

from .views import (data_package_list, data_package_create, data_package_delete,
                    data_base, data_package_create1, children_ages_update,
                    package,
                    package_trips,
                    package_accommodation,
                    package_transport
                    )

app_name = 'package'


urlpatterns = [
    #=================================================================
    # PACOTES
    path('<city_destiny>/', data_base, name='data_base'),
    
    path('<city_destiny>/list/', package, name='package'),
    
    # Passeio
    path('<city_destiny>/list/trips/', package_trips, name='package_trips'),

    path('<city_destiny>/createbase/', data_package_create1, name='data_package_createOne'),
    path('<id_destiny>/create/', data_package_create, name='data_package_create'),
    path('<id_destiny>/list/', data_package_list, name='data_package_list'),

    path('<int:pk>/delete/', data_package_delete, name='data_package_delete'),

    path('<id_package>/children_ages_update/', children_ages_update, name='children_ages_update'),
    
    # Hospedagem
    path('<city_destiny>/list/accommodation/', package_accommodation, name='package_accommodation'),
    
    # Transporte
    path('<city_destiny>/list/transport/', package_transport, name='package_transport'),
]