from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("username", "text", "image")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("user_sender", "receiver_group", "message")
