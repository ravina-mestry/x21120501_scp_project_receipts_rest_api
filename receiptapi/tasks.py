from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def sendmyemail(actionName, receiptName, dateReceipt, merchantName, amountTotal, userEmail):
    subject = 'Receipt Notification - ' + actionName + ': ' + merchantName
    message = 'RECEIPT for ' + receiptName + '\n'
    message = message + 'Date: ' + dateReceipt + '\n'
    message = message + 'Merchant: ' + merchantName + '\n'
    message = message + 'Amount: €' + str(amountTotal) + '\n' + '\n'
    if actionName == 'ADD':
        message = message + 'Thank you for adding receipt.'
    else:
        message = message + 'Thank you for updating receipt.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [userEmail,]
    result = send_mail(subject, message, email_from, recipient_list)
    return True;
