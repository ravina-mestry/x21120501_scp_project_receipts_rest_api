from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def sendmyemail(actionName, userEmail):
    subject = 'Receipt Notification 101 ' + actionName
    message = 'Thank you for sending receipt'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [userEmail,]
    result = send_mail(subject, message, email_from, recipient_list)
    return True;
