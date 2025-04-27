from django.urls import path
from . import views
urlpatterns = [
    path('send-emails/', views.SendCustomEmails.as_view(), name='send-emails'),
]
