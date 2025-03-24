from django.shortcuts import render
from rest_framework import viewsets,permissions
from . import models
from . import serializers

# Create your views here.

class GalleryViewset(viewsets.ModelViewSet):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAdminUser()]
        return []
    

