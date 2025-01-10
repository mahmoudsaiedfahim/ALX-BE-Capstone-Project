from django.shortcuts import render

from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework import status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Review
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name'] # search by name
    #filterset_fields = ['category', 'price']
    filterset_fields = {
        'category':['exact'],
        'price':['gte','lte'], # greater than or equal  price__gte=30000
        'stock_quantity':['gt','lt'],} # greater than

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product_id=product_id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    