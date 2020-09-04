from rest_framework import serializers, pagination
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'name',
                  'last_name',
                  )


class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100
