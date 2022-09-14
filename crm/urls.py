from django.urls import path
from .views import (UserListApiView,
                    CategoryListApiView,
                    VendorApiView)

urlpatterns = [
    path('user_list/', UserListApiView.as_view(), name='user-list'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat-list'),
    path('vendor_list/', VendorApiView.as_view(), name='vendor-list'),
]