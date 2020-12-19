from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.api.permissions.is_owner import IsOwnerOrReadOnly
from apps.drawings.models.tickets import Ticket
from apps.products.models.products import Product
from apps.products.serializers.products import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    # TODO: Test it

    def perform_create(self, serializer):
        instance = serializer.save()

        # Creating drawing tickets.
        if serializer.validated_data['available_for_drawing']:
            if serializer.validated_data['price'] <= 1000:
                n = 100
            elif 1000 <= serializer.validated_data['price'] <= 10000:
                n = 1000
            else:
                n = 10000

            Ticket.objects.bulk_create([Ticket(product=instance)] * n)

    def perform_update(self, serializer):
        # Prevents updating `price` and `available_for_drawing` fields.
        serializer.validated_data.pop('price')
        serializer.validated_data.pop('available_for_drawing')
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        # Prevents destroying product which has been sponsored.
        instance = self.get_object()
        if Ticket.objects.filter(~Q(user=None), product=instance).exists():
            return Response(
                'You can not delete product which has been sponsored already.', status=status.HTTP_403_FORBIDDEN
            )

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
