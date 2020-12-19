from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.cart.models.models import Cart
from apps.users.models.profiles import Profile
from apps.users.serializers.users import RegistrationUserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """ Initializing User and Token"""

    queryset = User.objects.all()
    serializer_class = RegistrationUserSerializer

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

        token = Token.objects.get_or_create(user=user)[0]

        return Response({'id': user.username, 'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)
