from django.db import models

from apps.products.models.products import Product
from apps.users.models.profiles import Profile


class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    price_sum = models.PositiveSmallIntegerField('Amount', default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('Last modified', auto_now=True)

    def __str__(self):
        return f'{self.profile.user.username} cart'
