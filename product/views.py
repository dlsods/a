from rest_framework.generics import *
from product.models import Product
from product.serializers import ProductListSerializer


class ProductsListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
