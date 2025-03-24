from . import models
from rest_framework import serializers

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsLetter
        fields = '__all__'