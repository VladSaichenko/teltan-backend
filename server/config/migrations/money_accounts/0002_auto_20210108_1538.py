# Generated by Django 3.1.4 on 2021-01-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Balance'),
        ),
    ]
