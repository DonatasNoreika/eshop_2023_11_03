from django.shortcuts import render, reverse
from django.views import generic
from .models import Product, Order, OrderLine
from django.contrib.auth.mixins import LoginRequiredMixin

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

class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    fields = ['status']
    template_name = "order_form.html"
    success_url = "/orders/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class OrderLineCreateView(LoginRequiredMixin, generic.CreateView):
    model = OrderLine
    fields = ['product', 'quantity']
    template_name = "orderline_form.html"
    success_url = "/orders/"

    def get_success_url(self):
        return reverse('order', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)


