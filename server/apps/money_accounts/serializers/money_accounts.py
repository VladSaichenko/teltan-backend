from rest_framework import serializers

from apps.money_accounts.models.money_accounts import MoneyAccount


class MoneyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoneyAccount
        fields = ('id', 'balance')
