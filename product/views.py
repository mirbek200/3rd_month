from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework import permissions, status, generics
from django.core.paginator import Paginator
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


class ProductListApiView(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,  request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page_num = self.request.query_params.get('page')
        print(page_num)
        serializers = ProductSerializer(paginator.page(page_num), many=True)
        return Response(serializers.data)


class ProductFilterApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name', 'price']


class ProductCreateApiView(APIView):

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializers = ProductSerializer(post)
        data = serializers.data
        return Response(data)


class ProductUpdateApiView(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = ProductSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryCreateApiView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = self.get_object(name)
        products = Product.objects.filter(category__name=name)
        serializer = CategorySerializer(category)
        serializer2 = ProductSerializer(products, many=True)
        data = serializer.data
        data['products'] = serializer2.data
        return Response(data)


class CategoryUpdateApiView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteApiView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PriceApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, price):
        prod = Product.objects.filter(price=price)
        serializers = ProductSerializer(prod, many=True)
        data = serializers.data
        return Response(data)

