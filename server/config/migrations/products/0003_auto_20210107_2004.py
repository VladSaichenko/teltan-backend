# Generated by Django 3.1.4 on 2021-01-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201219_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
    ]
