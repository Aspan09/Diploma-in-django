from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment, UserNet, Message
from .serializers import PostSerializer, CommentSerializer, UserNetSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly, IsOwnerForMessageReadOnly


# UserView
class UserNetAPIList(generics.ListCreateAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class UserNetAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserNetAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = UserNet.objects.all()
    serializer_class = UserNetSerializer
    permission_classes = (IsAdminOrReadOnly, )


# PostView
class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly, )


# CommentView
class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentAPIUpdate(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CommentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminOrReadOnly, )


# MessageView
class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class MessageAPIUpdate(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


class MessageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


