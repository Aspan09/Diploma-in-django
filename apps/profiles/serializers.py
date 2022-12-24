from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserNet


class UserNetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserNet
        fields = ("username", "user", "email", "first_name", "last_name", "avatar", "phone")

