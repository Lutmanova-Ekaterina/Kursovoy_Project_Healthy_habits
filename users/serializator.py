from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'email', 'password', 'first_name', 'last_name', 'telegram_id')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        """переопределим, чтобы хешировался пвроль"""
        return User.objects.create(email=validated_data['email'],
                                   password=validated_data['password'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'],
                                   telegram_id=validated_data['telegram_id'])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            # fields обязательный - Список или кортеж имен полей, которые должны составлять уникальный набор. Они должны существовать как поля в классе сериализатора.
            'first_name',
            'last_name',
            'email',
        )
