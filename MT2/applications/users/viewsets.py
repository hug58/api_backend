from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer, UserPagination


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination
