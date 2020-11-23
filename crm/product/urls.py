from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    products, 
    createProduct,
    updateProduct,
    deleteProduct,
    createTag,
)

urlpatterns = [
    path('products/', products, name='products'),
    path('create_product/', createProduct, name='create_product'),
    path('update_product/<str:pk>', updateProduct, name='update_product'),
    path('delete_product/<str:pk>', deleteProduct, name='delete_product'),

    path('create_tag/', createTag, name='create_tag'),
]
