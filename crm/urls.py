from django.urls import path
from .views import (UserListView,
                    CategoryListApiView,
                    )

urlpatterns = [
    path('user_list/', UserListView.as_view(), name='user-list'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat-list'),
]