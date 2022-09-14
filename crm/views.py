from django.contrib.auth.models import User
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer
from user.serializers import UserSerializers, AccountSerializers
from user.permissions import *


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        user_list = []
        for i in users:
            user_list.append(i.username)

        username = len(user_list)

        data = {
            "users": username,
        }
        return Response(data)

class CategoryListApiView(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class PriceApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for i in products:
            price_list.append(i.price)
        max_price = max(price_list)
        min_price = min(price_list)
        avg_price = sum(price_list) / len(price_list)

        data = {
            "max_price": max_price,
            "min_price": min_price,
            "avg_price": avg_price,
        }
        return Response(data)


class AvgPriceApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for i in products:
            price_list.append(i.price)
        avg_price = sum(price_list) / len(price_list)

        data = {
            "avg_price": avg_price

        }
        return Response(data)


class MinPriceApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for i in products:
            price_list.append(i.price)
        min_price = min(price_list)

        data = {
            "min_price": min_price
        }
        return Response(data)


class MaxPriceApiView(APIView):

    def get(self, request):
        products = Product.objects.all()
        price_list = []
        for i in products:
            price_list.append(i.price)
        max_price = max(price_list)


        data = {
            "max_price": max_price
        }
        return Response(data)


class Revenue(APIView):

    def get(self, request):
        products = Product.objects.all()
        revenue = []
        for i in products:
            one = i.price * i.quantity
            revenue.append(one)
        revenue = sum(revenue)

        data = {
            "revenue": revenue
        }
        return Response(data)


class LenProduct(APIView):

    def get(self, request):
        products = Product.objects.all()
        posts = []
        for i in products:
            posts.append(i.id)

        product = len(posts)

        data = {
            "product": product
        }
        return Response(data)
