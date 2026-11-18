from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import UserAccount


class UserAccountSerializer(UserCreateSerializer):
    password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True
    )

    class Meta(UserCreateSerializer.Meta):
        model = UserAccount
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'address'
        )


class UserAccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'address'
        )