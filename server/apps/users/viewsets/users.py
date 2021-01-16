from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from apps.api.permissions.is_users_profile import IsUsersProfile
from apps.cart.models.models import Cart
from apps.money_accounts.models.money_accounts import MoneyAccount
from apps.users.models.profiles import Profile
from apps.users.serializers.users import RegistrationUserSerializer, PublicUserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """ Initializing User, Token, Profile, Cart, MoneyAccount"""

    queryset = User.objects.all()
    serializer_class = RegistrationUserSerializer
    permission_classes = (IsUsersProfile,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = User(
            username=serializer.validated_data['username'],
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            email=serializer.validated_data['email'],
        )
        user.set_password(serializer.validated_data['password'])
        user.save()

        Profile.objects.create(
            user=user,
            phone_num_code=serializer.validated_data['profile']['phone_num_code'],
            phone_num=serializer.validated_data['profile']['phone_num'],
        )

        Cart.objects.create(user=user)
        MoneyAccount.objects.create(user=user)

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            'user': PublicUserSerializer(user).data,
            'token': token.key,
        }, status=status.HTTP_201_CREATED)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'user': PublicUserSerializer(user).data,
            'token': token.key,
        })


class PublicUserViewSet(mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PublicUserSerializer
    permission_classes = (IsUsersProfile,)
    queryset = User.objects.all()
