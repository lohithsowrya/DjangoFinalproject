from django.urls import path
from .views import place_order, order_success, my_orders, admin_orders

urlpatterns = [
    path("place/", place_order, name="place_order"),
    path("success/", order_success, name="order_success"),
    path("my-orders/", my_orders, name="my_orders"),
    path("admin-orders/", admin_orders, name="admin_orders"),
]
