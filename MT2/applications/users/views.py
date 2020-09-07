from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import User
from rest_framework.authtoken.models import Token


class ListUsers(ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        return User.objects.all()


class RegisterUser(APIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, created = User.objects.get_or_create(
            username=serializer.data.get("username"),
            email=serializer.data.get("email"),
            name=serializer.data.get("name"),
            last_name=serializer.data.get("last_name"),
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
