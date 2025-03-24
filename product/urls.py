from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'brands', views.BrandViewset)

urlpatterns = [
    path('', include(router.urls)),
]
