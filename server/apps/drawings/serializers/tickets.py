from rest_framework import serializers

from apps.drawings.models.tickets import Ticket
from apps.products.models.products import Product


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=False, read_only=False)

    class Meta:
        model = Ticket
        fields = ('id', 'product', 'user')
