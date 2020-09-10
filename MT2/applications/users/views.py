from .serializers import UserSerializer, UserSerializer2
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import User
from applications.friends.models import Friends
from rest_framework.authtoken.models import Token


class RegisterUser2(APIView):
    serializer_class = UserSerializer2
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, created = User.objects.get_or_create(
            username=serializer.validated_data['username'],
            name=serializer.validated_data['name'],
            last_name=serializer.validated_data['last_name'],
            email=serializer.validated_data['email'],
            is_active=True,
        )
        if created:

            token = Token.objects.create(user=user)
        else:

            token = Token.objects.get(user=user)

        user_get = {
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'last_name': user.last_name,
        }

        friends = serializer.validated_data['friends']
        user_id = User.objects.get(id=user.pk)
        for friend in friends:
            Friends.objects.get_or_create(
                name=friend["name"],
                last_name=friend['last_name'],
                city=friend['city'],
                status=friend['status'],
                friend=user_id,
            )
        return Response({
            "status": 200,
            "message": "user and friends added",
            "token": token.key,
            "user": user_get,
            "friends": friends})


class RegisterUser(APIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data.get("friends"))

        user, created = User.objects.get_or_create(
            username=serializer.data.get("username"),
            email=serializer.data.get("email"),
            name=serializer.data.get("name"),
            last_name=serializer.data.get("last_name"),
            password="super",
            is_active=True,
        )

        if created:

            token = Token.objects.create(user=user)
        else:

            token = Token.objects.get(user=user)

        user_get = {
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'last_name': user.last_name,
        }

        return Response({"token": token.key,
                         "user": user_get})
