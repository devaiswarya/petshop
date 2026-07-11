from django.db import models
from order.models import Order
from products.models import Products

# Create your models here.
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderitem')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='orderitem')
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'orderitem'
