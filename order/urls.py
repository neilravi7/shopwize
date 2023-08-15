from django.urls import path
app_name = 'order'

from .import views

urlpatterns=[
    path('start_order/', views.start_order, name='start_order'),
    path('detail/<slug:order_display_id>/', views.OrderDetailView.as_view(), name='order_details'),
]