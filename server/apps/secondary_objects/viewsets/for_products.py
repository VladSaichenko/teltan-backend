from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.secondary_objects.models.for_products import Category
from apps.secondary_objects.serializers.for_products import CategorySerializer


class CategoryViewSet(RetrieveModelMixin,
                      ListModelMixin,
                      GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
