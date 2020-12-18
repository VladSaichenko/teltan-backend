from django.db import models

from apps.money_accounts.models.money_accounts import MoneyAccount


class Transaction(models.Model):
    money_account = models.ForeignKey(
        MoneyAccount, verbose_name='Account', related_name='transactions', on_delete=models.PROTECT
    )
    amount = models.DecimalField('Balance', max_digits=7, decimal_places=2)
    created = models.DateTimeField('Created', auto_now_add=True)

    def __str__(self):
        return f'{self.money_account} at {self.created}'
