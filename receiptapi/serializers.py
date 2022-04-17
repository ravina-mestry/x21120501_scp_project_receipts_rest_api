from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'name', 'date_receipt', 'merchant_name', 'amount_total', 'user', 'user_email')
