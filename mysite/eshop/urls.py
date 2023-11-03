from django.contrib import admin
from django.urls import path, include
from .views import ProductListView, OrderListView, OrderDetailView

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path('orders/', OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name="order"),
]