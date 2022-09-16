from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from product.models import Product
from .models import Account
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, AccountSerializers
from .permissions import AnonPermissionOnly
from .serializers import UserSerializers
from rest_framework import permissions, generics
from rest_framework.generics import (
    CreateAPIView
)
from product.serializers import ProductSerializer


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializer


# class RegisterApiView(CreateAPIView):
#     queryset = Account.objects.all()
#     permission_classes = (AnonPermissionOnly,)
#     serializer_class = AccountSerializers

class RegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = AccountSerializers(data=request.data)
        if serializers.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email']
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                phone_number=request.data['phone_number'],
            )
            account.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailApi(APIView):

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        serializers = UserSerializers(user)
        data = serializers.data
        return Response(data)


class UserListApiView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializers(users, many=True)
        return Response(serializers.data)



class UserFilterApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']


