from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from rest_framework import permissions
from .models import Receipt
from .serializers import ReceiptSerializer
from .tasks import sendmyemail

# Create your views here.
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print('create' + serializer.validated_data['user_email'])
        sendmyemail.delay('CREATE', serializer.validated_data['user_email'])
        serializer.save()
    
    def perform_update(self, serializer):
        print('update' + serializer.validated_data['user_email'])
        sendmyemail.delay('UPDATE', serializer.validated_data['user_email'])
        serializer.save()

def email(request):
    sendmyemail.delay()
    return HttpResponse('Success!')
