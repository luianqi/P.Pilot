from rest_framework import generics, status, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User
from apps.users.permissions import IsSuperuser
from apps.users.serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsSuperuser]

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

        # Perform user authentication check
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if not user:
            return Response(
                {"ошибка": "Пользователь не найден!"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.check_password(password):
            return Response(
                {"ошибка": "Неверный пароль"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        # Authentication successful, generate tokens and return response
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


class GetUsersView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    """
    Returns a list of admins and managers.
    Also provides detail view and filter.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    filterset_fields = ["role"]

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)