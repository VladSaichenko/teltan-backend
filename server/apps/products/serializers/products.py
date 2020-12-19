from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault

from apps.products.models.products import Product, ProductImage
from django.contrib.auth.models import User


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')


class ProductSerializer(ModelSerializer):
    product_images = PrimaryKeyRelatedField(many=True, read_only=True)
    user = PrimaryKeyRelatedField(queryset=User.objects.all(), default=CurrentUserDefault())

    class Meta:
        model = Product
        fields = (
            'id', 'user', 'name', 'description', 'main_image', 'price', 'category', 'year',
            'age_restriction', 'available_for_drawing', 'created', 'product_images'
        )
        extra_kwargs = {
            'user': {'read_only': True},
            'product_images': {'read_only': True}
        }
