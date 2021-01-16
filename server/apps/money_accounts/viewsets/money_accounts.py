from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.api.permissions.is_owner import IsOwner
from apps.money_accounts.models.money_accounts import MoneyAccount
from apps.money_accounts.serializers.money_accounts import MoneyAccountSerializer


class MoneyAccountViewSet(ListModelMixin,
                          GenericViewSet):
    serializer_class = MoneyAccountSerializer
    queryset = MoneyAccount.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return MoneyAccount.objects.filter(user=self.request.user)
