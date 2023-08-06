from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexListView, ProductsDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='list'),
    path('view/<int:pk>/', ProductsDetailView.as_view(), name='view'),
]