from django.urls import path
from django.contrib.auth import views as auth_views

from . views import( 
orders,
createOrder,
createOrderCustomer, 
updateOrder,
deleteOrder,
)


urlpatterns = [

    path('orders/', orders, name='orders'),
    path('create_order/', createOrder, name='create_order'),
    path('create_order_customer/<str:pk>/', createOrderCustomer, name='create_order_customer'),
    path('update_order/<str:pk>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),
    
]
