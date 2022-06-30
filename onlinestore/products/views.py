from django.http import JsonResponse
from django.shortcuts import render


from .models import Product, Manufacture

def product_list(request): #the problem using this and not the drf is that it shows limited data. Ex. It does not show photo url only its name; Does not show data content of manu
    products = Product.objects.all()#[:5]
    data = {'products':list(products.values())} #can specify the data or value that we want to get. add params in values
    response = JsonResponse(data)
    return response

def product_detail(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product':{
            'name': product.name,
            'manufacturer': product.manufacturer.name,
            'description':product.description,
            'photo': product.photo.url,
            'price':product.price,
            'shippinh_cost':product.shipping_cost,
            'quantity':product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            'error':{
                'code':404,
                'message':'product not found!'
            }}, 
            status=404)
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