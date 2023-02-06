from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("Пользователь не найден!")

        if not user.check_password(password):
            raise AuthenticationFailed("Неверный пароль")

        refresh = RefreshToken.for_user(user)
        is_superuser = user.is_superuser

        return Response(
            {
                "role": user.role,
                "id": user.pk,
                "is_superuser": is_superuser,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )