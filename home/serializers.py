from rest_framework import serializers
from .models import ProductModel, PostModel
from django.contrib.auth import get_user_model

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'Date')
        model = ProductModel


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModel

        fields = ('id', 'title1', 'body', 'pro')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')