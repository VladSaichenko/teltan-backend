from rest_framework import serializers

from apps.users.models.profiles import Profile


class ProfileSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('phone_num_code', 'phone_num', 'address')


class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'picture')
