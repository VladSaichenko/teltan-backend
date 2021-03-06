# Generated by Django 3.1.4 on 2021-01-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age_restriction',
            field=models.PositiveSmallIntegerField(choices=[(0, '0+'), (6, '6+'), (12, '12+'), (16, '16+'), (18, '18+')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_draw',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
