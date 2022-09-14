from django.urls import path
from .views import (ProductListApiView,
                    ProductCreateApiView,
                    ProductDetailApiView,
                    ProductUpdateApiView,
                    CategoryCreateApiView,
                    ProductDestroyApiView,
                    CategoryApiView,
                    PriceApiView,
                    CategoryUpdateApiView,
                    ProductFilterApiView)

urlpatterns = [
    path('prod_list/', ProductListApiView.as_view(), name='prod-list'),
    path('prod_create/', ProductCreateApiView.as_view(), name='prod-create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('update/<int:id>/', ProductUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', ProductDestroyApiView.as_view(), name='delete'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('cat_update/', CategoryUpdateApiView.as_view(), name='cat_update'),
    path('filter_cat/<slug:name>/', CategoryApiView.as_view(), name='filter_category'),
    path('filter_price/<int:price>/', PriceApiView.as_view(), name='filter-price'),
    path('filter_product/', ProductFilterApiView.as_view(), name='filter-product'),
]
