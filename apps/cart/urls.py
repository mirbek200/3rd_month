from django.urls import path
from .views import (
    AddToCartAPIView, PayToCartAPIView,
)

urlpatterns = [
    path('add_to_cart/<int:id>/', AddToCartAPIView.as_view(), name='add-to-cart'),
    path('pay_to_cart/<int:user_id>/', PayToCartAPIView.as_view(), name='pay-to-cart'),
]
