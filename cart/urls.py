from django.urls import path
from .views import create_cartproduct,fetch_userproduct,update_cart,delete_cartproduct

urlpatterns=[
    path('create/',create_cartproduct,name='create_cartproduct'),
    path('fetch/',fetch_userproduct,name='fetch_userproduct'),
    path('update/<int:pk>/',update_cart,name='update_cart'),
    path('delete/<int:pk>/',delete_cartproduct,name='delete_cartproduct'),
]