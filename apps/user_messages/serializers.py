from rest_framework import serializers
from profiles.models import UserNet
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=UserNet.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=UserNet.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'data_send']




