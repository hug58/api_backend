from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from .serializers import FriendsSerializer
from .models import Friends
# Create your views here.


class ListFriends(ListAPIView):
    serializer_class = FriendsSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Friends.objects.list_friends_users(username)
