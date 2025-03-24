from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class ContactUsView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        if not name or not email or not message:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        subject = f'New message from {name}'
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = [settings.SUPPORT_EMAIL]
        
        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,  
            recipient_list,
            fail_silently=False,
        )

        return Response({"message": "Thank you for contacting us! Your message has been sent."}, status=status.HTTP_200_OK)