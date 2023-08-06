# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


# def index(request):
#     context = {
#         'object_list': Product.objects.all()
#     }
#     return render(request, 'catalog/product_list.html', context)

class IndexListView(ListView):
    model = Product


# def products(request, pk):
#     products_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'{products_item}'
#     }
#     return render(request, 'catalog/product_detail.html', context)

class ProductsDetailView(DetailView):
    model = Product
