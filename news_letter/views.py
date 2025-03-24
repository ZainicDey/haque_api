from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers, models
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class NewsLetterView(APIView):
    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        serializer = serializers.NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            news_letter = get_object_or_404(models.NewsLetter, pk=pk)
            serializer = serializers.NewsLetterSerializer(news_letter)
        else:
            news_letters = models.NewsLetter.objects.all()
            serializer = serializers.NewsLetterSerializer(news_letters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        if not request.user.is_staff:
            return Response({"message": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        news_letter = models.NewsLetter.objects.get(pk=pk)
        serializer = serializers.NewsLetterSerializer(news_letter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response({"message": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        news_letter = get_object_or_404(models.NewsLetter, pk=pk)
        news_letter.delete()
        return Response({"message": "Newsletter deleted successfully"}, status=status.HTTP_200_OK)
