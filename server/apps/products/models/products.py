from django.contrib.auth.models import User
from django.db import models

from apps.secondary_objects.models.for_products import Category


class Product(models.Model):
    AGE_RESTRICTION_CHOICES = (
        (0, '0+'),
        (6, '6+'),
        (12, '12+'),
        (16, '16+'),
        (18, '18+'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    description = models.TextField()
    main_image = models.ImageField(upload_to='product_main_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField(null=True)
    age_restriction = models.PositiveSmallIntegerField(choices=AGE_RESTRICTION_CHOICES)

    is_draw = models.BooleanField(default=False)
    tickets_amount = models.PositiveSmallIntegerField(default=0)
    tickets_bought = models.PositiveSmallIntegerField(default=0)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    redemption_percent = models.PositiveSmallIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    viewed = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images')
