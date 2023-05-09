from response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializator import UserSerializer, RegisterSerializer


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    # permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
             "message": "User Created Successfully.",
        })


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = []


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = []


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()  # queryset обязательный - Это набор запросов, в отношении которого должна обеспечиваться уникальность.
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]
