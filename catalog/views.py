from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/index.html', context)

def products(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)
