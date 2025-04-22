from django.conf import settings
from django.core.mail import send_mass_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class SendCustomEmails(APIView):
    def post(self, request):
        if not request.user.is_staff:
            return Response({"message": "You are not authorized to perform this action"}, status=status.HTTP_403_FORBIDDEN)
        
        # Get the list of user IDs from the request data, if provided
        user_ids = request.data.get("user_ids", [])
        message = request.data.get("message")
        
        # If user_ids is provided, filter users based on those IDs; otherwise, get all users
        if user_ids:
            users = User.objects.filter(id__in=user_ids)
        else:
            users = User.objects.all()
        
        email_messages = [
            (f"Hello {user.name}", f"Dear {user.name}, {message}",
            settings.EMAIL_HOST_USER, [user.email])
            for user in users
        ]
        
        send_mass_mail(email_messages, fail_silently=False)
        return Response({"message": "Emails sent successfully"}, status=status.HTTP_200_OK)
