from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import UserSendMessageInGroup, Group


class UserSendMessageInGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSendMessageInGroup
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"
