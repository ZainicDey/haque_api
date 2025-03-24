from django.conf import settings
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def send_custom_emails(APIView):
    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        users = User.objects.all()
        message = request.data.get("message")
        email_messages = [
            (f"Hello {user.name}", f"Dear {user.name}, {message}",
            settings.EMAIL_HOST_USER, [user.email])
            for user in users
        ]
        send_mass_mail(email_messages, fail_silently=False)
        return Response({"message": "Emails sent successfully"}, status=status.HTTP_200_OK)
