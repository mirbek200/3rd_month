from django.urls import path
from .views import (UserListView,
                    CategoryListApiView,
                    AvgPriceApiView,
                    MinPriceApiView,
                    MaxPriceApiView,
                    PriceApiView,
                    Revenue,
                    LenProduct)

urlpatterns = [
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat-list'),
    path('avg/',  AvgPriceApiView.as_view(), name='avg'),
    path('min/',  MinPriceApiView.as_view(), name='min'),
    path('max/',  MaxPriceApiView.as_view(), name='max'),
    path('spatistic/',  PriceApiView.as_view(), name='statistic'),
    path('revenue/',  Revenue.as_view(), name='revenue'),
    path('len_product/', LenProduct.as_view(), name='products'),

]


