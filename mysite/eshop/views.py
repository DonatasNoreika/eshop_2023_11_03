from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"