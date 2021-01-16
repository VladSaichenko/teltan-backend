from rest_framework.serializers import ModelSerializer

from apps.money_accounts.models.transactions import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'money_account', 'amount', 'created')
