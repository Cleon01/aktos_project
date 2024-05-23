from rest_framework import serializers
from .models import Account, Consumer, Client

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['name']

class AccountSerializer(serializers.ModelSerializer):
    consumers = ConsumerSerializer(many=True)

    class Meta:
        model = Account
        fields = ['client', 'consumers', 'balance', 'status']