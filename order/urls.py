from django.urls import path
from .views import create_order,fetch_order,update_order,order_detail

urlpatterns=[
    path('create/',create_order,name='create_order'),
    path('fetch/',fetch_order,name='fetch_order'),
    path('update/<int:pk>/',update_order,name='update_order'),
    path('detail/<int:pk>/',order_detail,name='order_detail'),
]
