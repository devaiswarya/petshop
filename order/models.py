from django.db import models
from user.models import User

# Create your models here.
class Order(models.Model):
    STATUS=[
        ('Placed','Placed'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
    status=models.CharField(max_length=100,choices=STATUS,default='Placed')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
