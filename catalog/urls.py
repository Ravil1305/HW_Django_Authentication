from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('view/<int:pk>/', ProductsDetailView.as_view(), name='view'),
    path('catalog/create/', ProductsCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductsUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),
]
