from django.shortcuts import render
from .models import (
    Catalog, 
    Product,
    )
from rest_framework import viewsets, permissions

from .serializers import (
    CatalogSerializer,
    ProductSerializer,
    
)
class NotSafeMethodAndAllowAny(permissions.AllowAny):
    def has_permission(self, request, view):
        return (view.action in [ 'list']
                and super(NotSafeMethodAndAllowAny, self).has_permission(request, view))

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer