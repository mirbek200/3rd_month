import stripe
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import Http404, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cart.models import Cart, Order
from apps.cart.serializers import CartSerializer
from third_month import settings


class AddToCartAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CartSerializer

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, id):
        snippet = self.get_object(id)
        serializer = CartSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def get_object(self, id):
        try:
            return Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            raise Http404

    def post(self,request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        cart = self.get_object(product_id)
        # product = ProductSerializer(cart.product.all(), many=True)
        # Cart.objects.aggregate(Sum('price'))
        price = cart.product.all().aggregate(Sum('price'))
        print(price)

        product = {}
        product['id'] = product_id
        product['name'] = 'order'
        product['price'] = price

        order = Order.objects.create(
            name=product['name']+str(Order.pk),
            price=product['price']['price__sum']
        )
        order.save()

        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product['price']['price__sum']*100,
                        'product_data': {
                            'name': product['name']
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product['id']
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class PayToCartAPIView(TemplateView):
    permission_classes = [permissions.AllowAny]
    template_name = "landing.html"

    def get_object(self, user_id):
        try:
            return Cart.objects.get(customer_id=user_id)
        except Cart.DoesNotExist:
            raise Http404

    def get_context_data(self, user_id, **kwargs):
        cart = self.get_object(user_id)
        # product = ProductSerializer(cart.product.all(), many=True)
        # Cart.objects.aggregate(Sum('price'))
        price=cart.product.all().aggregate(Sum('price'))

        product={}
        product['id']=user_id
        product['name']='order'
        product['price']=price
        context = super(PayToCartAPIView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context

