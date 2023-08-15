from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/details.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'