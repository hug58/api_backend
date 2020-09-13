from abc import ABC

from rest_framework import serializers, pagination
from .models import User
from applications.friends.serializers import FriendsSerializer


class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    friends = FriendsSerializer(many=True)

