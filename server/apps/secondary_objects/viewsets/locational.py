from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.secondary_objects.models.locational import Country
from apps.secondary_objects.serializers.locational import CountrySerializer


class CountryViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
