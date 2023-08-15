import random
import time
from django.db import models
from helpers.models import BaseModel
from django.conf import settings
from products.models import Product
# Create your models here.

class Order(BaseModel):

    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)
    order_display_id = models.CharField(max_length=20, unique=True, null=True)

    class Meta:
        db_table = 'orders'
        ordering = ("-created_at",)
    
    def save(self, *args, **kwargs):
        if not self.order_display_id:
            timestamp = str(int(time.time()))
            rand_num = str(random.randint(100000, 999999))
            self.order_display_id = timestamp + rand_num
        super().save(*args, **kwargs)


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'order_items'