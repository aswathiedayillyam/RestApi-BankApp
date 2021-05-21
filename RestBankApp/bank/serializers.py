from rest_framework.serializers import ModelSerializer
from .models import User, Accounts, Transactions
from rest_framework import serializers


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class BankAccountModelSerializer(ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['account_num', 'user_name', 'balance', 'acnt_type']


class TransactionSerializer(serializers.Serializer):
    account_number = serializers.CharField()
    to_acno = serializers.IntegerField()
    amount = serializers.IntegerField()
    date = serializers.DateField(required=False)

    def create(self, validated_data):
        acno = validated_data["account_number"]
        acnt_obj = Accounts.objects.get(account_number=acno)
        validated_data["account_number"] = acnt_obj
        return Transactions.objects.create(**validated_data)


class WithdrawSerializer(serializers.Serializer):
    amount = serializers.IntegerField()


class DepositSerializer(serializers.Serializer):
    amount = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()