from django.shortcuts import render
from .models import PostModel, ProductModel
from .serializers import PostSerializers, ProductSerializers, UserSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
# Create your views here.
from django.contrib.auth import get_user_model

class ProductListView(ListCreateAPIView):
    queryset = ProductModel.objects.all()

    serializer_class = ProductSerializers


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()

    serializer_class = ProductSerializers



class PostListView(ListCreateAPIView):
    queryset = PostModel.objects.all()

    serializer_class = PostSerializers


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()

    serializer_class = PostSerializers


class UserListView(ListCreateAPIView):
    queryset = get_user_model().objects.all()

    serializer_class = UserSerializers


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()

    serializer_class = UserSerializers

# class ProductViewset(ModelViewSet):
#     queryset = ProductModel.objects.all()
#
#     serializer_class = ProductSerializers
#
#
# class PostViewset(ModelViewSet):
#     queryset = PostModel.objects.all()
#
#     serializer_class = PostSerializers
#
#
# class UserViewset(ModelViewSet):
#     queryset = get_user_model().objects.all()
#
#     serializer_class = UserSerializers