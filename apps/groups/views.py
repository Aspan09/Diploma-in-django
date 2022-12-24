from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import UserSendMessageInGroup, Group
from .serialaizers import UserSendMessageInGroupSerializer, GroupSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class UserSendMessageInGroupSerializerAPIList(generics.ListCreateAPIView):
    queryset = UserSendMessageInGroup.objects.all()
    serializer_class = UserSendMessageInGroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class UserSendMessageInGroupSerializerAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserSendMessageInGroup.objects.all()
    serializer_class = UserSendMessageInGroupSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserSendMessageInGroupSerializerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = UserSendMessageInGroup.objects.all()
    serializer_class = UserSendMessageInGroupSerializer
    permission_classes = (IsAdminOrReadOnly, )


class GroupAPIList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class GroupAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class GroupAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminOrReadOnly, )