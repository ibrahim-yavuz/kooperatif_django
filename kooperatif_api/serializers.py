from rest_framework import serializers
from .models import Payer, PayRecord


class PayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payer
        fields = ('first_name', 'second_name', 'shares', 'phone_number', 'added_time')


class PayRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayRecord
        fields = ('payer', 'paid_shares', 'pay_date')


