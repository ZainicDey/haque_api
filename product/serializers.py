from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=models.Category.objects.all()
    )
    class Meta:
        model = models.Product
        fields = ['id', 'name', 'description', 'category', 'images', 'price', 'stock', 'created_at', 'updated_at']
    def get_images(self, obj):
        return [img.image for img in obj.images.all()]
