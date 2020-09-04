from rest_framework import serializers, pagination
from .models import Friends


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('__all__')


class FriendsPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100
