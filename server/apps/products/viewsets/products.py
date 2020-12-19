from rest_framework.viewsets import ModelViewSet
from apps.products.models.products import Product
from apps.products.serializers.products import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # TODO: Add permissions
