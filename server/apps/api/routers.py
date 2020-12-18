from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets.users import UserViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('user', UserViewSet, basename='user')
