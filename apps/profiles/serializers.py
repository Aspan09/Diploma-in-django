from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment, UserNet, Message


class UserNetSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserNet
        fields = ("username", "email", "first_name", "last_name", "avatar", "phone")


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("username", "text", "image")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=UserNet.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=UserNet.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
