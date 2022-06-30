from itertools import product
from django.urls import path
from .views import manufacture_list,manufacture_detail, product_detail,product_list

urlpatterns = [
    path('products/',product_list, name='product-list'),
    path('products/<int:pk>/',product_detail, name='product-detail'),
    path('manufacture/',manufacture_list, name='manufacture-list'),
    path('manufacture/<int:pk>/',manufacture_detail, name='manufacture-detail'),


]