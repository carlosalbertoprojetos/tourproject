from django.urls import path


from .views import (category_register, trip_register,
                    trip_list, trip_details, trip_update)

# trip_delete


app_name = 'trip'


urlpatterns = [
    path('category/', category_register, name="category_register"),
    
    path('register/', trip_register, name='trip_register'),
    path('list/', trip_list, name='trip_list'),
    path('<int:pk>/details/', trip_details, name='trip_details'),
    path('<int:pk>/edit/', trip_update, name='trip_update'),
    # path('<int:pk>/delete/', trip_delete, name='trip_delete'),
]