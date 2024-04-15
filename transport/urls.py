from django.urls import path

from .views import (
    transport_category_delete,
    transport_category_list_create,
    transport_category_update,
    transport_catpax_delete,
    transport_catpax_list_create,
    transport_catpax_update,
    transport_delete,
    transport_list_create,
    transport_price_delete,
    transport_price_list_create,
    transport_price_update,
    transport_update,
)

app_name = "transport"

urlpatterns = [
    path(
        "category/list/",
        transport_category_list_create,
        name="transport_category_list_create",
    ),
    path(
        "category/update/<int:pk>/",
        transport_category_update,
        name="transport_category_update",
    ),
    path(
        "category/delete/<int:pk>/",
        transport_category_delete,
        name="transport_category_delete",
    ),
    path(
        "categorypax/list/",
        transport_catpax_list_create,
        name="transport_catpax_list_create",
    ),
    path(
        "categorypax/edit/<int:pk>/",
        transport_catpax_update,
        name="transport_catpax_update",
    ),
    path(
        "categorypax/delete/<int:pk>/",
        transport_catpax_delete,
        name="transport_catpax_delete",
    ),
    path("list/", transport_list_create, name="transport_list_create"),
    path("update/<int:pk>/", transport_update, name="transport_update"),
    path("delete/<int:pk>/", transport_delete, name="transport_delete"),
    path(
        "price_transport/list/",
        transport_price_list_create,
        name="transport_price_list_create",
    ),
    path(
        "price_transport/update/<int:pk>/",
        transport_price_update,
        name="transport_price_update",
    ),
    path(
        "price_transport/delete/<int:pk>/",
        transport_price_delete,
        name="transport_price_delete",
    ),
]
