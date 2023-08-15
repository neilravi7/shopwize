from django.urls import path
app_name = 'cart'

from .import views

urlpatterns=[
    path('', views.cart, name='cart'),
    path('add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update-cart/<uuid:product_id>/<str:action>/', views.update_cart, name='update_cart'),
    path('hx_menu_cart', views.hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total', views.hx_cart_total, name='hx_cart_total'),
    path('checkout/success/', views.payment_success, name='payment_sucess'),
    path('checkout/cancel/', views.payment_cancel, name="payment_cancel"),
]