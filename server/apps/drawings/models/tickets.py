from django.db import models

from apps.products.models.products import Product
from apps.users.models.profiles import Profile


class Ticket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.product} {self.profile}'
