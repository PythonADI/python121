
from django.urls import path
from store.views import product_list_view

urlpatterns = [
    path("products/", product_list_view, name="product_list"),
]
