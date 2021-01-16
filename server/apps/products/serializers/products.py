from rest_framework import serializers

from apps.products.models.products import Product, ProductImage
from apps.users.serializers.users import PublicUserSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')


class ProductSerializer(serializers.ModelSerializer):
    product_images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = PublicUserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = (
            'id', 'user', 'name', 'description', 'main_image', 'price', 'category', 'year', 'age_restriction',
            'is_draw', 'tickets_amount', 'tickets_bought', 'redemption_percent', 'created', 'product_images',
            'viewed', 'ticket_price'
        )
        extra_kwargs = {
            'user': {'read_only': True},
            'tickets_amount': {'read_only': True},
            'tickets_bought': {'read_only': True},
            'ticket_price': {'read_only': True},
            'redemption_percent': {'read_only': True},
            'product_images': {'read_only': True},
            'viewed': {'read_only': True}
        }
