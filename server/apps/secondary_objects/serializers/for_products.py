from rest_framework.serializers import ModelSerializer

from apps.secondary_objects.models.for_products import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
