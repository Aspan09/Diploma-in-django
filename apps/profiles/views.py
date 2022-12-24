from django.shortcuts import render
from rest_framework import generics
from .models import UserNet
from .serializers import UserNetSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


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

