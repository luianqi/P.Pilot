from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperuser(BasePermission):
    message = "Пользователь должен быть суперадмином"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdmin(BasePermission):
    message = "Пользователь должен быть админом"

    def has_permission(self, request, view):
        if (
            request.method in SAFE_METHODS
            or request.user.is_anonymous
            or request.user.role == "Админ"
        ):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == "Админ":
            return True
        if request.user.is_anonymous and request.method in SAFE_METHODS:
            return True
        return False