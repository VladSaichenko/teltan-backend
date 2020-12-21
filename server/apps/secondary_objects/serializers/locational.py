from rest_framework.serializers import ModelSerializer

from apps.secondary_objects.models.locational import Country


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'icon')
