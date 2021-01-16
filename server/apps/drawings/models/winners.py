from django.contrib.auth.models import User
from django.db import models

from apps.products.models.products import Product


class Winner(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

