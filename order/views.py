import json
import stripe

from django.http import JsonResponse
from django.conf import settings
from django.views.generic import DetailView

from cart.cart import Cart
from .models import Order, OrderItem


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_details.html'
    context_object_name = 'order'
    slug_field = 'order_display_id'
    slug_url_kwarg = 'order_display_id'


def start_order(request):
    print('# Initialize cart object')
    cart = Cart(request)
    data = json.loads(request.body)
    total_price = 0

    items = []

    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])
        # in stripe payment 199 is 19900 
        stripe_price = int(product.price)
        stripe_price = str(stripe_price)+"00"
        
        items.append({
            'price_data':{
                'currency':'usd',
                'product_data':{
                    'name':product.name
                },
                'unit_amount':int(stripe_price)
            },
            'quantity':item['quantity']
        })
    
    # initailize stripe"
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    # Initialize checkout session"
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url = 'http://127.0.0.1:8000/cart/checkout/success',
        cancel_url='http://127.0.0.1:8000/cart/checkout/cancel/'        
    )
    
    # creating payment intent"
    payment_intent = session.payment_intent    
    
    order_data = {
        'user': request.user,
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'email': data.get('email'),
        'address': data.get('address'),
        'zipcode': data.get('zipcode'),
        'place': data.get('city'),
        'phone': data.get('phone'),
    }


    # creating order
    order = Order.objects.create(**order_data)
    order.payment_intent = payment_intent
    order.price = total_price
    order.paid_amount = total_price
    order.paid = True
    order.save()

    # creating order items:
    for item in cart:
        product = item['product']
        item_dict = {
            'order': order,
            'product': product,
            'price': product.price * int(item['quantity']),
            'quantity': int(item['quantity'])
        }

        item = OrderItem.objects.create(**item_dict)
    
    # Clearing cart 
    cart.clear()

    # return session id to checkout page
    return JsonResponse(
        {'session':session, 'order':payment_intent}
    )