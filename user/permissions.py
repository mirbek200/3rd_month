from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from user.models import PhoneNumber


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already authenticated"

    def has_permission(self, request, view):
        return not request.user.is_authenticated









