from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from url_filter.integrations.drf import DjangoFilterBackend


from apps.products.models.products import ProductImage
from apps.products.serializers.products import ProductImageSerializer


class ProductImageViewSet(RetrieveModelMixin,
                          ListModelMixin,
                          GenericViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product',)
