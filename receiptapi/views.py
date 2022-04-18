from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from rest_framework import permissions
from .models import Receipt
from .serializers import ReceiptSerializer

# Create your views here.
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]
    
def email(request):
    subject = 'Receipt Notification'
    message = 'Thank you for sending receipt'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sach.mestry@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse('Success!')
