from django.urls import path

from . import views

app_name = 'client'

urlpatterns = [   
     
    path('list/', views.list_view),
    
    #path('register/', RegisterClientView.as_view(), name='client_register'),

    #path('<int:pk>/edit/', UpdateClientView.as_view(), name='client_edit'),
]