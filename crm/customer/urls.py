from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    customer, 
customers, 
createCustomer,
deleteCustomer,
updateCustomer
)

urlpatterns = [
    path('customers/', customers, name='customers'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('create_customer/', createCustomer, name='create_customer'),
    path('customer_update/<str:pk>', updateCustomer, name='update_customer'),
    path('customer_delete/<str:pk>', deleteCustomer, name='delete_customer'),
    
]
