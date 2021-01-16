from django.db import models

from django.contrib.auth.models import User


class MoneyAccount(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='money_account', on_delete=models.PROTECT)
    balance = models.DecimalField('Balance', max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username
