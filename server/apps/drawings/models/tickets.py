from django.contrib.auth.models import User
from django.db import models

from apps.products.models.products import Product


class Ticket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
