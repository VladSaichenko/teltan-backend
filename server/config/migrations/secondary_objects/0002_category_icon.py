# Generated by Django 3.1.4 on 2020-12-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary_objects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='category_icons'),
        ),
    ]
