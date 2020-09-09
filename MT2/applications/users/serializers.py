from rest_framework import serializers, pagination
from .models import User
from applications.friends.serializers import FriendsSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        friends = FriendsSerializer(many=True, read_only=False)
        fields = ('username',
                  'email',
                  'name',
                  'last_name',
                  'friends',
                  )


class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100
