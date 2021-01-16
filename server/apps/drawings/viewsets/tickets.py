from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.drawings.models.tickets import Ticket
from apps.drawings.serializers.tickets import TicketSerializer
from apps.money_accounts.models.money_accounts import MoneyAccount


class TicketViewSet(CreateModelMixin,
                    GenericViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    # TODO: Test it.

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        price = serializer.validated_data['product'].ticket_price
        account = MoneyAccount.objects.get(user=self.request.user)
        if account.balance >= price:
            account.balance -= price
            account.save(update_fields=['balance'])

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response({'error': 'You do not have enough money on your account'}, status=status.HTTP_403_FORBIDDEN)
