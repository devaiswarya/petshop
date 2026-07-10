from django.db import models
from user.models import User
from products.models import Products

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='cart')
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Cart'

