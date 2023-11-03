from django.shortcuts import render
from django.views import generic
from .models import Product, Order

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"


class OrderListView(generic.ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = "order"

