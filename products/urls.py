from django.urls import path
from .views import create_product,fetch_product,get_product,update_product,delete_product,product_one

urlpatterns=[
    path('create/',create_product,name='create_product'),
    path('fetch/',fetch_product,name='fetch_product'),
    path('get/',get_product,name='get_product'),
    path('product/<int:pk>/',product_one,name='product_one'),
    path('update/<int:pk>/',update_product,name='update_product'),
    path('delete/<int:pk>/',delete_product,name='delete_product'),
]