from common.models import Account
from rest_framework import serializers
from .service import add_balance_to_account, subtract_from_account_balance


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('balance', 'status')


class AccountAddBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('balance', )

    def update(self, instance, validated_data):
        return add_balance_to_account(instance, validated_data.get('balance'))


class AccountSubtractBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('balance', )
        
    def update(self, instance, validated_data):
        return subtract_from_account_balance(instance, validated_data.get('balance'))
