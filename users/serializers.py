from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Username cannot be empty."
            )
        return value.strip()

    def validate_email(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Email cannot be empty."
            )
        return value.strip()

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )