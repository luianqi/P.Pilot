from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    message = "Пользователь должен быть суперадмином"

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)