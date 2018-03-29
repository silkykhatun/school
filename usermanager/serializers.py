"""Serializers for UserManager."""
import logging

from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password
User = get_user_model()
logger = logging.getLogger('main')


class UserSerializer(serializers.ModelSerializer):
    """Main Serializer for User Model."""

    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()

    class Meta:
        """Meta class for the serializer."""

        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

    def save(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        email = validated_data.get('email', None)
        try:
            user = User.objects.create(
                username=username, email=email,
                password=make_password(password, salt="mk28"))
            return user
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def validate(self, attrs):
        """Check for existing username and email."""
        if 'username' in attrs:
            if User.objects.filter(username=attrs['username']):
                raise serializers.ValidationError("Username Already Taken.")
        if 'email' in attrs:
            if User.objects.filter(email=attrs['email']):
                raise serializers.ValidationError("Email Already Taken.")
        return attrs
