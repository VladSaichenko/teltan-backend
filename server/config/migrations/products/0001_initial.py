# Generated by Django 3.1.4 on 2020-12-19 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secondary_objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('main_image', models.ImageField(upload_to='product_main_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('age_restriction', models.PositiveSmallIntegerField(choices=[(0, '0+'), (6, '6+'), (12, '12+'), (16, '16+'), (18, '18+')], verbose_name='Age restrictions')),
                ('available_for_drawing', models.BooleanField(default=False, verbose_name='Is available for drawing')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondary_objects.category', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
