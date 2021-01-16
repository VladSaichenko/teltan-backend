from rest_framework import routers

from apps.products.viewsets.product_images import ProductImageViewSet
from apps.products.viewsets.products import ProductViewSet
from apps.secondary_objects.viewsets.for_products import CategoryViewSet
from apps.secondary_objects.viewsets.locational import CountryViewSet
from apps.test.viewsets import TestViewSet
from apps.users.viewsets.users import PublicUserViewSet
from apps.users.viewsets.users import UserViewSet
from apps.money_accounts.viewsets.money_accounts import MoneyAccountViewSet
from apps.drawings.viewsets.tickets import TicketViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('user', UserViewSet, basename='user')
router.register('product', ProductViewSet, basename='product')
router.register('product-image', ProductImageViewSet, basename='product-image')
router.register('public-user', PublicUserViewSet, basename='public_user')
router.register('category', CategoryViewSet, basename='category')
router.register('country', CountryViewSet, basename='country')
router.register('money-account', MoneyAccountViewSet, basename='money-account')
router.register('ticket', TicketViewSet, basename='ticket')
