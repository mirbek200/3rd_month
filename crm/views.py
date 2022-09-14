from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer
from user.serializers import UserSerializers, AccountSerializers
from user.permissions import *
from user.models import Account


class UserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)


class CategoryListApiView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class VendorApiView(APIView):
    def get(self, request):
        users = Account.objects.all()
        serializers = AccountSerializers(users, many=True)
        return Response(serializers.data)
