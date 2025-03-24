from django.shortcuts import render
from django.http import HttpResponse
from . import models, serializers
from rest_framework import viewsets,filters,permissions,status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__name', 'brand__name']
    search_fields = ['name', 'description', 'category__description', 'brand__description']
    ordering_fields = ['original_price', 'created_at']

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAdminUser()]
        return []

    def create(self, request, *args, **kwargs):
        image_data = request.data.pop('images', [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        for image_url in image_data:
            models.Image.objects.create(product=product, image=image_url)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAdminUser()]
        return []
    def create(self, request, *args, **kwargs):
        category_name = request.data.get('name').lower()
        if models.Category.objects.filter(name=category_name).exists():
            return Response({'error': 'Category already exists'},status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(name=category_name) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BrandViewset(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAdminUser()]
        return []