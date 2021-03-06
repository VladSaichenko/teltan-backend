# Generated by Django 3.1.4 on 2020-12-19 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Balance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='money_account', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Balance')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('money_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='money_accounts.moneyaccount', verbose_name='Account')),
            ],
        ),
    ]
