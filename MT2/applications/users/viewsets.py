from rest_framework import viewsets
from .models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer, UserPagination



class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination
