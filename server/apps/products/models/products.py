from django.db import models

from apps.secondary_objects.models.for_products import Category
from apps.users.models.profiles import Profile


class Product(models.Model):
    AGE_RESTRICTION_CHOICES = (
        (0, '0+'),
        (6, '6+'),
        (12, '12+'),
        (16, '16+'),
        (18, '18+'),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=65)
    description = models.TextField('Description')
    main_image = models.ImageField(upload_to='product_main_images')
    price = models.DecimalField('Price', max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Year')
    age_restriction = models.PositiveSmallIntegerField('Возрастное ограничение', choices=AGE_RESTRICTION_CHOICES)
    available_for_drawing = models.BooleanField('Is available for drawing', default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
