from django.urls import path
from . import views
urlpatterns = [
    path('send-emails/', views.send_custom_emails, name='send-emails'),
]
