from django.contrib.auth.models import User
from rest_framework import serializers

from apps.users.serializers.profiles import ProfileSerializer


class RegistrationUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
