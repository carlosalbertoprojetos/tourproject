from django.urls import path

from .views import (data_base, 
                    children_ages_update,
                    package,
                    package_trips,
                    package_accommodation,
                    package_transport,
                    package_concluded
                    )

app_name = 'package'


urlpatterns = [
    path('<city_destiny>/', data_base, name='data_base'),
    path('list/<city_destiny>/', package, name='package'),
    path('<city_destiny>/trips/list/', package_trips, name='package_trips'),
    path('<id_package>/children_ages_update/', children_ages_update, name='children_ages_update'),    
    path('<city_destiny>/accommodation/', package_accommodation, name='package_accommodation'),    
    path('<city_destiny>/transport/', package_transport, name='package_transport'),    
    path('<id_package>/concluded/', package_concluded, name='package_concluded'),    
]