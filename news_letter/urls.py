from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsLetterView.as_view(), name='newsletter'),
    path('<int:pk>', views.NewsLetterView.as_view(), name='newsletter-detail'),
]
