from django.urls import path
from django.contrib.auth import views as auth_views

from . views import( 
registerPage, 
loginPage, 
logoutUser, 
home, 
userPage, 
products, 
createProduct,
updateProduct,
deleteProduct,
customer, 
customers, 
createCustomer,
deleteCustomer,
updateCustomer,
createTag,
orders,
createOrder,
createOrderCustomer, 
updateOrder,
deleteOrder,
)

urlpatterns = [

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('', home, name='home'),
    path('user', userPage, name='user-page'),

    path('products/', products, name='products'),
    path('create_product/', createProduct, name='create_product'),
    path('update_product/<str:pk>', updateProduct, name='update_product'),
    path('delete_product/<str:pk>', deleteProduct, name='delete_product'),

    path('customers/', customers, name='customers'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('create_customer/', createCustomer, name='create_customer'),
    path('customer_update/<str:pk>', updateCustomer, name='update_customer'),
    path('customer_delete/<str:pk>', deleteCustomer, name='delete_customer'),

    path('create_tag/', createTag, name='create_tag'),


    path('orders/', orders, name='orders'),
    path('create_order/', createOrder, name='create_order'),
    path('create_order_customer/<str:pk>/', createOrderCustomer, name='create_order_customer'),
    path('update_order/<str:pk>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
]