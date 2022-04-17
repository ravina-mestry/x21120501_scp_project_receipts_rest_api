from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests

# Create your views here.
def receipts(request):
    url = settings.RECEIPT_API_URL + '/receipts/?format=json'
    headers = {'Authorization': settings.RECEIPT_API_TOKEN}
    response = requests.get(url, headers=headers)
    #convert reponse data into json
    receipts = response.json()
    print(receipts)
    return HttpResponse(receipts)
