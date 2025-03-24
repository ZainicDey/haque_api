from django.urls import path
from . import views

urlpatterns = [
    path('api/newsletter/', views.NewsLetterView.as_view(), name='newsletter'),
    path('api/newsletter/<int:pk>/', views.NewsLetterView.as_view(), name='newsletter-detail'),
]
