from rest_framework.generics import GenericAPIView
import re
from account.models import User
from account.serializers import RegisterSerializer, LoginSerializer, AddUser

from rest_framework import response, status, permissions, viewsets
from django.contrib.auth import authenticate


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@+northsouth.edu')
        serializer = self.serializer_class(data=request.data)
        if User.objects.filter(is_superuser=True).exists():
            return response.Response({'message': "You can't register for admin"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():

                if re.fullmatch(regex, serializer.validated_data["email"]):
                    serializer.save()
                    return response.Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    response.Response({'message': "You can't register for admin"}, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addUser(GenericAPIView):
    authentication_classes = []
    serializer_class = AddUser

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@+northsouth.edu')
        if serializer.is_valid():
            if re.fullmatch(regex, serializer.validated_data["email"]):
                if serializer.validated_data["role"] == "teacher":
                    serializer.validated_data["is_admin"] = True
                    serializer.save()
                    return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return response.Response({'message': "You can't register for This app"},
                                         status=status.HTTP_400_BAD_REQUEST)



        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
