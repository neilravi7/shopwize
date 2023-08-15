from django.urls import path
app_name = 'products'

from .import views

urlpatterns=[
    path('details/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
]