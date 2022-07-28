from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from numpy import product
from .models import Product, category
from math import ceil
from django.db.models import Count

# Create your views here.
def index(request):
    Categories = category.objects.all()
    products = Product.objects.all()
    n = len(products)
    nSlides = n//3 + ceil((n/3)-(n//3))
    nc = len(Categories)//2
    params = {'myproducts': products, 'no_of_slides': nSlides, 'range': range((nSlides)), 'Categories': Categories, 'crange': range(nc)}
    return render(request, 'shop/Home1.html', params)

def test(request):
    products = Product.objects.filter(product_name__icontains = 'Nikon')
    Categories = category.objects.all()
    p = []
    for x in Categories:
        p.append(products.filter(product_category = x))
    params = {'Categories': Categories, 'Prod': p}
    return render(request, 'shop/test.html', params)

def Productviewer(request):
    Categories = category.objects.all()
    Brand_name = request.GET.get('b_name', 'NA')
    products = Product.objects.filter(product_name__icontains = Brand_name)
    p = []
    for x in Categories:
        p.append(products.filter(product_category = x))
    params = {'b_name': Brand_name, 'Prod': p, 'Cat': Categories}
    return render(request, 'shop/Productviewer.html', params)