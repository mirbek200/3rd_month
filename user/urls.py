from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from user.views import (
    RegisterView,
    MyObtainPairView,
    UserDetailApi,
    RegisterApiView,
    UserListApiView,
    UserFilterApiView
)


urlpatterns = [
    path('user_list/', UserListApiView.as_view(), name='user-list'),
    path('user_filter/', UserFilterApiView.as_view(), name='user-filter'),
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_detail/<int:id>/', UserDetailApi.as_view(), name='user-detail'),
    path('vendor_register/', RegisterApiView.as_view(), name='vendor_register'),
]