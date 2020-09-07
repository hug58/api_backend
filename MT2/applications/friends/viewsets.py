from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Friends
from .serializers import FriendsSerializer, FriendsPagination


class FriendsViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = FriendsSerializer
    queryset = Friends.objects.all()
    pagination_class = FriendsPagination