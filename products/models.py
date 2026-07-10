from django.db import models
from category.models import Category

# Create your models here.
class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")
    product_name=models.CharField(max_length=200)
    brand=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    is_avaliable=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

