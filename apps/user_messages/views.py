from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerForMessageReadOnly
from .models import Message
from .serializers import MessageSerializer


# MessageView
class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


class MessageAPIUpdate(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


class MessageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerForMessageReadOnly, )


