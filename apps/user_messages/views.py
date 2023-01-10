from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerForMessageReadOnly, PrivateMessageReadonly
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


class MessagesAPIPrivate(generics.ListCreateAPIView):

    def get(self, request, user_name):
        m = Message.objects.filter(sender__username=user_name)
        m2 = Message.objects.filter(receiver__username=user_name)

        return Response({
            'message_sender': MessageSerializer(m, many=True).data,
            'message_receiver': MessageSerializer(m2, many=True).data
        })

    serializer_class = MessageSerializer
    permission_classes = (PrivateMessageReadonly,)
