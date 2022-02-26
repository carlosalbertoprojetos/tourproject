from django.urls import path

from .views import (category_register, product_details, product_register,
                    product_update, products_list)

# product_delete


app_name = 'product'


urlpatterns = [
    path('category/', category_register, name="category_register"),
    
    path('register/', product_register, name='product_register'),
    path('list/', products_list, name='products_list'),
    path('<int:pk>/detail/', product_details, name='product_details'),
    path('<int:pk>/edit/', product_update, name='product_update'),
    # path('<int:pk>/delete/', product_delete, name='product_delete'),
]
