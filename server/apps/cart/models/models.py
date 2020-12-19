from django.db import models

from django.contrib.auth.models import User
from apps.products.models.products import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    price_sum = models.PositiveSmallIntegerField('Amount', default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('Last modified', auto_now=True)

    def __str__(self):
        return f'{self.user.username} cart'
