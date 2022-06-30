from django.http import JsonResponse
from django.shortcuts import render


from .models import Product, Manufacture

def product_list(request): 
    products = Product.objects.all()#[:5]
    data = {'products':list(products.values())} #can specify the data or value that we want to get. add params in values
    response = JsonResponse(data)
    return response
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# Create your views here.
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'

# class ProductListView(ListView):
#     model = Product 
#     template_name = 'products/product_list.html'