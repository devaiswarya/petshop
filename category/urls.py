from django.urls import path
from .views import create_category,fetch_category,update_category,delete_category

urlpatterns=[
    path("create/",create_category,name='create_category'),
    path('fetch/',fetch_category,name='fetch_category'),
    path('update/<int:pk>/',update_category,name='update_category'),
    path('delete/<int:pk>/',delete_category,name='delete_category'),
]